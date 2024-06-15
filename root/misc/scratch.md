# a css scratchpad

i make the software that makes every graphic on this website. i make some of it
in css and then take a screenshot. here's some of that.

favicon:

<div style="width:26px;height:26px;border:3px solid
#0f0;background:#000;font:20px
monospace;text-align:center;line-height:26px;font-weight:bold;">
JB
</div>

johnvertisement

<div style="width:728px;height:90px;position:relative;font-weight:bold;">
<div style="z-index:-1;position:absolute;width:20%;height:100%;background:linear-gradient(rgba(255,0,0),rgba(0,255,0))"></div>
<div style="z-index:-1;position:absolute;width:20%;height:100%;background:linear-gradient(90deg,rgba(255,255,0),rgba(0,0,255));left:20%"></div>
<div style="z-index:-1;position:absolute;width:20%;height:100%;background:linear-gradient(45deg,rgba(0,0,0) 0%,rgba(255,0,255) 10%,rgba(0,255,0) 20%,rgba(128,128,128) 30%,rgba(31,99,59) 40%,rgba(255,0,0) 50%,rgba(100,0,255) 60%,rgba(0,100,0) 70%,rgba(198,4,0) 80%,rgba(33,106,98) 90%,rgba(255,255,255));left:40%"></div>
<div style="z-index:-1;position:absolute;width:20%;height:100%;background:linear-gradient(100deg,rgba(159,123,0),rgba(159,123,0) 30%,rgba(100,192,11) 60%,rgba(100,192,11));left:60%"></div>
<div style="z-index:-1;position:absolute;width:20%;height:100%;background:linear-gradient(rgba(0,0,0),rgba(90,215,204));left:80%"></div>
<div style="position:absolute">jazzybones<br>HAS MADE</div>
<div style="position:absolute;left:30%;top:45%">A SERIES OF<br>UNPLEASANT<br>GRADIENTS</div>
<div style="position:absolute;left:46%;top:40%;transform:rotate(45deg);font-size:9pt">AS A DEFENSIVE<br>MECHANISM</div>
<div style="position:absolute;left:57%;top:30%;transform:rotate(-90deg)">FOR THEIR</div>
<!--
<div style="position:absolute;left:80%;top:0%;width:20%;font-weight:normal;font-size:8px">crippling social anxiety that someone will find this shitty fucking website and click it and think that it's fucking awful oh my fucking god what the fuck am i even doing with this website i feel like i'm relying on gimmicks to get clicks there's nothing actually here i'm just some nerd writing html by hand</div>
-->
<div style="position:absolute;left:80%;top:0%;width:20%;font-weight:normal;font-size:8px">crippling social anxiety that i don't have enough substance as a character like i try to let my personality shine through and make the site memorable but i feel like i have to rely on silly gimmicks to get people to click on and that's leaving me deeply unfulfilled like what am i even doing you know?</div>
</div>

88x31 button (this requires javascript to properly render)

<div class=jbimg><pre>
88 31
88x31.png
2
G rgba(0,255,0,255)
  rgba(0,0,0,255)
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG|
G                                                                                      G|
G                                                                                      G|
G                         GGGG               GGGGG  GGG  GGGGG GGGGG G   G             G|
G                     GGGG   G                 G   G   G    G     G   G G              G|
G                 GGGG       G                 G   GGGGG   G     G     G               G|
G             GGGG      GGGG G               G G   G   G  G     G      G               G|
G         GGGG      GGGG   G G                G    G   G GGGGG GGGGG   G               G|
G     GGGG      GGGG       G G                                                         G|
G     G     GGGG           G G                                                         G|
G     G GGGG               G G               GGGG   GGG  G   G GGGGG  GGGG             G|
G     G G                  G G               G   G G   G GG  G G     G                 G|
G     G G                  G G               GGGG  G   G G G G GGGGG  GGG              G|
G     G G                  G G               G   G G   G G  GG G         G             G|
G     G G                GGG G               GGGG   GGG  G   G GGGGG GGGG              G|
G     G G            GGGG    G                                                         G|
G     G G        GGGG     GGGG                                                         G|
G     G G    GGGG     GGGG    GG                                                       G|
G     G GGGGG     GGGG      G   GG                                                     G|
G     G G     GGGG      GGGG GG   GG             GGGGGG                                G|
G     G   GGGG      GGGG       GG   GG          GGGGGGGG                               G|
G     GGGG      GGGG         GGGGG    GG       G  GGGG  G     G       G   G GGGGG      G|
G      GG   GGGG         GGGG        GGGG     G  G GG  G G   G        GG GG G          G|
G        GG   GGG    GGGG   GG   GGGG         G    GG    G  GGGGGGGGG G G G GGGGG      G|
G          GG   GGGGG   GG   GGGG             GG  GGGG  GG   G        G   G G          G|
G            GG          GGGG                 GGGGGGGGGGGG    G       G   G GGGGG      G|
G              GG    GGGG                     GGGGGGGGGGGG                             G|
G                GGGG                         GGGGGGGGGGGG                             G|
G                                              GG  GG  GG                              G|
G                                                                                      G|
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG|
</pre></div>

<script>
const IMG_CLASS="jbimg";

function renderImage(dest, content) {
	// read metadata
	lines = content.textContent.split('\n');
	currLine = 0
	dims = lines[currLine++].split(' ');
	if (dims.length != 2) {
		return;
	}
	width = Number(dims[0]);
	height = Number(dims[1]);
	fileName = lines[currLine++];
	numColors = Number(lines[currLine++]);
	colors = {};
	for (let i = 0; i < numColors; ++i) {
		colorString = lines[currLine++]
		colors[colorString[0]] = colorString.substring(1)
	}

	// create canvas
	canvas = document.createElement("canvas");
	dest.appendChild(canvas);
	ctx = canvas.getContext("2d");
	ctx.canvas.width = width;
	ctx.canvas.height = height;

	// draw image
	for (let y = 0; y < height; ++y) {
		line = lines[currLine++];
		if (line.length != width+1) {
			return;
		}
		for (let x = 0; x < width; ++x) {
			pix = line[x];
			ctx.fillStyle = colors[pix];
			ctx.fillRect(x, y, 1, 1);
		}
	}

	// create download link
	linkContainer = document.createElement("p");
	link = document.createElement("a");
	link.href = canvas.toDataURL("image/png");
	link.download = fileName;
	link.innerText = "download this image";
	linkContainer.appendChild(link)
	dest.appendChild(linkContainer)
}

elems = document.getElementsByClassName(IMG_CLASS);
for (let i = 0; i < elems.length; ++i) {
	let elem = elems[i];
	for (let j = 0; j < elem.children.length; ++j) {
		child = elem.children[j];
		if (child.nodeName != "PRE") {
			continue;
		}
		renderImage(elem, child);
	}
}
</script>
