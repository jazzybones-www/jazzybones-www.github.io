# bitburner has consumed me

here's a bitburner script i wrote

```
import { enumerate } from "util.js";

// to run this program, you need to have all 5 port openers and formulas.exe
// just infiltrate megacorp and run buy -a

const INTERVAL = 10000;

const STOLEN_PER_CYCLE = 0.10;
const MONEY_THRESHOLD = 0.75;
const SECURITY_THRESHOLD = 5;
const MAX_DEPTH = -1;

const INITIAL_SERVER_SIZE = 256;

/*
this code creates a timesharing system with all the hosts of a network

a "job" is either a grow, weaken, or hack operation. they have the following schema

{
  "type": "grow" | "weaken" | "hack",
  "host": [string, the host name],
  "threads": [number, the number of threads to use],
  "priority": [number, the profit/millisecond/gb used],
  "callback": [function, run when this job is complete],
  "atomic": [boolean, true if this job should NOT be split],
}
*/

let pendingJobs = [];
let ownedServers = [];

function jobToMemory(job) {
  switch(job) {
  case "grow":
    return 1.75;
  case "weaken":
    return 1.75;
  case "hack":
    return 1.70;
  }
}

/** @param {NS} ns */
function runJob(ns, host, job, threads) {
  switch (job.type) {
  case "grow": ns.exec("atom-grow.js", host, threads, job.host); break;
  case "weaken": ns.exec("atom-weaken.js", host, threads, job.host); break;
  case "hack": ns.exec("atom-hack.js", host, threads, job.host); break;
  }
}

/** @param {NS} ns */
function getJobTime(ns, job) {
  switch (job.type) {
  case "grow": return ns.getGrowTime(job.host);
  case "weaken": return ns.getWeakenTime(job.host);
  case "hack": return ns.getHackTime(job.host);
  }
}

/** @param {NS} ns */
function allocateJobs(ns) {
  pendingJobs.sort((a, b) => {
    return a.priority - b.priority;
  });
  ns.print(pendingJobs);
  for (var i = 0; i < ownedServers.length; ++i) {
    var executingHost = ownedServers[i];
    var freeRam = ns.getServerMaxRam(executingHost) - ns.getServerUsedRam(executingHost);
    for (var j = pendingJobs.length - 1; j >= 0; --j) {
      var thisJob = pendingJobs[j];
      var thisJobRam = jobToMemory(thisJob.type);
      var maxCapacity = Math.floor(freeRam / thisJobRam);
      if (maxCapacity == 0) {
        continue;
      }
      if (thisJob.atomic && maxCapacity < thisJob.threads) {
        continue;
      }
      var threadsToUse = Math.min(maxCapacity, thisJob.threads);
      runJob(ns, executingHost, thisJob, threadsToUse);
      freeRam -= thisJobRam * threadsToUse;
      thisJob.threads -= threadsToUse;
      if (thisJob.threads == 0) {
        pendingJobs.splice(j, 1);
        setTimeout(thisJob.callback, getJobTime(ns, thisJob));
      }
    }
  }
}

/** @param {NS} ns */
async function manageHost(ns, host) {
  var maxMoney = ns.getServerMaxMoney(host);
  if (maxMoney == 0) {
    return;
  }
  var maxSecurity = ns.getServerMinSecurityLevel(host) + SECURITY_THRESHOLD;
  var minMoney = ns.getServerMaxMoney(host) * MONEY_THRESHOLD;
  var moneyPerCycle = maxMoney * STOLEN_PER_CYCLE;
  for (;;) {
    var cycleTime =
        getJobTime(ns, {"type": "grow", "host": host}) +
        getJobTime(ns, {"type": "hack", "host": host}) +
        getJobTime(ns, {"type": "weaken", "host": host});
    var moneyPerMs = moneyPerCycle / cycleTime;
    var callback;
    var promise = new Promise((resolve) => {
      callback = resolve;
    });

    var securityDiff = ns.getServerSecurityLevel(host) - maxSecurity;
    var currMoneyAvailable = ns.getServerMoneyAvailable(host);

    var threadCount = 1;
    var jobType = "weaken";
    var atomic = false;

    if (securityDiff > 0) {
      threadCount = Math.ceil(securityDiff / 0.05);
      jobType = "weaken";
    } else if (currMoneyAvailable < minMoney) {
      var multiplier = minMoney / currMoneyAvailable;
      threadCount = Math.ceil(ns.growthAnalyze(host, multiplier));
      jobType = "grow";
    } else {
      var hackThreads = ns.hackAnalyzeThreads(host, moneyPerCycle);
      jobType = "hack";
      threadCount = Math.ceil(hackThreads);
      atomic = true;
    }

    pendingJobs.push({
      type: jobType,
      host: host,
      threads: threadCount,
      priority: moneyPerMs / threadCount,
      callback: callback,
      atomic: atomic,
    });
    allocateJobs(ns);

    await promise;
  }
}

/** @param {NS} ns
 * tries to obtain root access and returns true if successful */
function canHack(ns, host) {
  if (ns.hasRootAccess(host)) {
    return false;
  }
  if (ns.getServerRequiredHackingLevel(host) > ns.getHackingLevel()) {
    return false;
  }

  ns.brutessh(host);
  ns.ftpcrack(host);
  ns.relaysmtp(host);
  ns.httpworm(host);
  ns.sqlinject(host);
  ns.nuke(host);
  return true;
}

function addOwnedServer(ns, host) {
  ns.scp(["atom-hack.js", "atom-grow.js", "atom-weaken.js"], host)
  
  ownedServers.push(host);
  manageHost(ns, host);
}

function scanHackAndManage(ns, serverList) {
  var didHack = false;
  for (var i = 0; i < serverList.length; ++i) {
    if (canHack(ns, serverList[i])) {
      addOwnedServer(ns, serverList[i]);
      didHack = true;
    }
  }
  if (didHack) {
    allocateJobs(ns);
  }
}

// bitburner will complain if we use ns.sleep
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

/** @param {NS} ns */
function shouldNotBuyServers(ns) {
  return ns.ls("home", "server-buy-lock").length != 0;
}

/** @param {NS} ns */
export async function main(ns) {
  var serverList = [];
  enumerate(ns, "home", MAX_DEPTH, function (host) {
    if (host == "home") {
      return;
    }
    serverList.push(host)
    if (ns.hasRootAccess(host)) {
      addOwnedServer(ns, host);
    }
  });
  var currServerSize = INITIAL_SERVER_SIZE;
  var maxServerSize = ns.getPurchasedServerMaxRam();
  for (;;) {
    scanHackAndManage(ns, serverList);
    allocateJobs(ns);
    for (;;) {
      if (shouldNotBuyServers(ns)) {
        break;
      }
      var newServer = ns.purchaseServer("autohack", currServerSize);
      if (newServer == "") {
        break;
      }
      addOwnedServer(ns, newServer);
      currServerSize = Math.min(currServerSize * 2, maxServerSize);
    }
    await sleep(INTERVAL);
  }
}
```

to use it, you need every single program purchased, including (i think, i
haven't actually checked) formulas.exe. you also need to have these three files
on your home system:

atom-hack.js

```
/** @param {NS} */
export async function main(ns) {
  await ns.hack(ns.args[0]);
}
```

atom-weaken.js

```
/** @param {NS} */
export async function main(ns) {
  await ns.weaken(ns.args[0]);
}
```

atom-grow.js

```
/** @param {NS} */
export async function main(ns) {
  await ns.grow(ns.args[0]);
}
```

i have been going way too deep into bitburner. this program essentially creates
a timesharing system to hack servers. the main process will automatically hack
servers, buy servers, rank servers, and send jobs to other servers.

the entire loop is based on "tasks". a task is some operation which needs to be
done, either a grow, weaken, or hack. these tasks can atomic or non-atomic.
atomic tasks need to be run by one process on one server, while non-atomic tasks
can be split across multiple servers in multiple threads. we have a bunch of
monitors that look at a single server and generate tasks to complete. then we
have a distributor which distributes the highest priority tasks to any available
servers.

the priority rating of each task is measured in dollars per millisecond per
gigabyte of execution, assuming that the dollars per millisecond is constant
across an entire grow() hack() weaken() cycle.

i'm starting to think that this hyperfixation is unhealthy.
