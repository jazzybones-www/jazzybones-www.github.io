# jb crypto part 4: frequency analysis, entropy, diffusion, and confusion

[read part 3 here](/blog/2024/06/27/0-discrete-log.html)

here's an encrypted message i just made

>     EZ ML ZG KZE EZ ML EASE YN EAL HULNEYZK
>     PALEALG EYN KZMQLG YK EAL JYKO EZ NUCCLG
>     EAL NQYKWN SKO SGGZPN ZC ZUEGSWLZUN CZGEUKL
>     ZG EZ ESXL SGJN SWSYKNE S NLS ZC EGZUMQLN
>     SKO MD ZIIZNYKW LKO EALJ EZ OYLEZ NQLLI
>     KZ JZGL SKO MD S NQLLI EZ NSD PL LKO
>     EAL ALSGESBAL SKO EAL EAZUNSKO KSEUGSQ NAZBXN
>     EASE CQLNA YN ALYG EZ EYN S BZKNUJJSEYZK
>     OLTZUEQD EZ ML PYNAO EZ OYL EZ NQLLI
>     EZ NQLLI ILGBASKBL EZ OGLSJSD EALGLN EAL GUM
>     CZG YK EASE NQLLI ZC OLSEA PASE OGLSJN JSD BZJL
>     PALK PL ASTL NAUCCQLO ZCC EAYN JZGESQ BZYQ
>     JUNE WYTL UN ISUNLEALGLN EAL GLNILBE
>     EASE JSXLN BSQSJYED ZC NZ QZKW QYCL
>     CZG PAZ PZUQO MLSG EAL PAYIN SKO NBZGKN ZC EYJL
>     EAZIIGLNNZGN PGZKW EAL IGZUO JSKN BZKEUJLQD
>     EAL ISKWN ZC OYNIGYFO QZTL EAL QSPN OLQSD
>     EAL YKNZQLKBL ZC ZCCYBL SKO EAL NIUGKN
>     EASE ISEYLKE JLGYE ZC EAUKPZGEAD ESXLN
>     PALK AL AYJNLQC JYWAE AYN HUYLEUN JSXL
>     PYEA S MSGL MZOXYK PAZ PZUQO CSGOLQN MLSG
>     EZ WGUKE SKO NPLSE UKOLG S PLSGD QYCL
>     MUE EASE EAL OGLSO ZC NZJLEAYKW SCELG OLSEA
>     EAL UKOYNBZTLGLO BZUKEGD CGZJ PAZNL MZUGK
>     KZ EGSTLQQLG GLEUGKN IUFFQLN EAL PYQQ
>     SKO JSXLN UN GSEALG MLSG EAZNL YQQN PL ASTL
>     EASK CQD EZ ZEALGN EASE PL XKZP KZE ZC
>     EAUN BZKNBYLKBL OZEA JSXL BZPSGON ZC UN SQQ
>     SKO EAUN EAL KSEYTL AUL ZC GLNZQUEYZK
>     YN NYBXQYLO ZLG PYEA EAL ISQL BSNE ZC EAZUWAE
>     SKO LKELGIGYNLN ZC WGLSE IYEA SKO JZJLKE
>     PYEA EAYN GLWSGO EALYG BUGGLKEN EUGK SPGD
>     SKO QZNL EAL KSJL ZC SBEYZK

to make it, i took some piece of english text and ran it through a "substitution
cipher". this means that i took every 'a' and turned them into some other
letter, took every 'b' and turned them into some other letter, and so on. let's
try and crack this message.

one interesting fact about english is that some letters are more common than
others. for example, in most text the letter 'e' shows up way more than the
letter 'z'. we know [the general distribution of letter frequencies in
english](https://en.wikipedia.org/wiki/Letter_frequency), so we can start by
measuring the letter frequencies of our encrypted message and working from
there.

    [L]: 136
    [E]: 118
    [Z]: 93
    [S]: 84
    [N]: 81
    [A]: 76
    [G]: 68
    [K]: 65
    [Y]: 53
    [O]: 42
    [Q]: 41
    [U]: 40
    [C]: 34
    [J]: 28
    [P]: 28
    [B]: 23
    [I]: 22
    [M]: 15
    [D]: 14
    [W]: 14
    [X]: 10
    [T]: 8
    [F]: 3
    [H]: 2
    total letters: 1098

the two most common letters in english are 'e' and 't', so we can reasonably
assume that the two most common letters in our ciphertext ('L' and 'E') map to
those. making those substitutions gives us this ciphertext:

    tZ Me ZG KZt tZ Me tASt YN tAe HUeNtYZK
    PAetAeG tYN KZMQeG YK tAe JYKO tZ NUCCeG
    tAe NQYKWN SKO SGGZPN ZC ZUtGSWeZUN CZGtUKe
    ZG tZ tSXe SGJN SWSYKNt S NeS ZC tGZUMQeN
    SKO MD ZIIZNYKW eKO tAeJ tZ OYetZ NQeeI
    KZ JZGe SKO MD S NQeeI tZ NSD Pe eKO
    tAe AeSGtSBAe SKO tAe tAZUNSKO KStUGSQ NAZBXN
    tASt CQeNA YN AeYG tZ tYN S BZKNUJJStYZK
    OeTZUtQD tZ Me PYNAO tZ OYe tZ NQeeI
    tZ NQeeI IeGBASKBe tZ OGeSJSD tAeGeN tAe GUM
    CZG YK tASt NQeeI ZC OeStA PASt OGeSJN JSD BZJe
    PAeK Pe ASTe NAUCCQeO ZCC tAYN JZGtSQ BZYQ
    JUNt WYTe UN ISUNetAeGeN tAe GeNIeBt
    tASt JSXeN BSQSJYtD ZC NZ QZKW QYCe
    CZG PAZ PZUQO MeSG tAe PAYIN SKO NBZGKN ZC tYJe
    tAZIIGeNNZGN PGZKW tAe IGZUO JSKN BZKtUJeQD
    tAe ISKWN ZC OYNIGYFO QZTe tAe QSPN OeQSD
    tAe YKNZQeKBe ZC ZCCYBe SKO tAe NIUGKN
    tASt IStYeKt JeGYt ZC tAUKPZGtAD tSXeN
    PAeK Ae AYJNeQC JYWAt AYN HUYetUN JSXe
    PYtA S MSGe MZOXYK PAZ PZUQO CSGOeQN MeSG
    tZ WGUKt SKO NPeSt UKOeG S PeSGD QYCe
    MUt tASt tAe OGeSO ZC NZJetAYKW SCteG OeStA
    tAe UKOYNBZTeGeO BZUKtGD CGZJ PAZNe MZUGK
    KZ tGSTeQQeG GetUGKN IUFFQeN tAe PYQQ
    SKO JSXeN UN GStAeG MeSG tAZNe YQQN Pe ASTe
    tASK CQD tZ ZtAeGN tASt Pe XKZP KZt ZC
    tAUN BZKNBYeKBe OZtA JSXe BZPSGON ZC UN SQQ
    SKO tAUN tAe KStYTe AUe ZC GeNZQUtYZK
    YN NYBXQYeO ZeG PYtA tAe ISQe BSNt ZC tAZUWAt
    SKO eKteGIGYNeN ZC WGeSt IYtA SKO JZJeKt
    PYtA tAYN GeWSGO tAeYG BUGGeKtN tUGK SPGD
    SKO QZNe tAe KSJe ZC SBtYZK

in english, certain pairs of letters go together very often, such as 'th', 'sh',
'en', and so on. these are called
[bigrams](https://en.wikipedia.org/wiki/Bigram) and can be used to continue our
journey. if we analyze all the bigrams in our ciphertext that start with 't', we
get this list:

    [tA]: 53
    [tZ]: 18
    [tY]: 10
    [tU]: 7
    [tS]: 7
    [tt]: 4
    [tG]: 4
    [tI]: 2
    [te]: 2
    [tP]: 2
    [tN]: 2
    [tJ]: 2
    [tW]: 1
    [tQ]: 1
    [tD]: 1
    [tO]: 1
    [tC]: 1

we can be pretty certain that the 'tA' bigram translates to 'th' in plaintext,
so we can reasonably deduce that 'A' translates to 'h'.

    tZ Me ZG KZt tZ Me thSt YN the HUeNtYZK
    PhetheG tYN KZMQeG YK the JYKO tZ NUCCeG
    the NQYKWN SKO SGGZPN ZC ZUtGSWeZUN CZGtUKe
    ZG tZ tSXe SGJN SWSYKNt S NeS ZC tGZUMQeN
    SKO MD ZIIZNYKW eKO theJ tZ OYetZ NQeeI
    KZ JZGe SKO MD S NQeeI tZ NSD Pe eKO
    the heSGtSBhe SKO the thZUNSKO KStUGSQ NhZBXN
    thSt CQeNh YN heYG tZ tYN S BZKNUJJStYZK
    OeTZUtQD tZ Me PYNhO tZ OYe tZ NQeeI
    tZ NQeeI IeGBhSKBe tZ OGeSJSD theGeN the GUM
    CZG YK thSt NQeeI ZC OeSth PhSt OGeSJN JSD BZJe
    PheK Pe hSTe NhUCCQeO ZCC thYN JZGtSQ BZYQ
    JUNt WYTe UN ISUNetheGeN the GeNIeBt
    thSt JSXeN BSQSJYtD ZC NZ QZKW QYCe
    CZG PhZ PZUQO MeSG the PhYIN SKO NBZGKN ZC tYJe
    thZIIGeNNZGN PGZKW the IGZUO JSKN BZKtUJeQD
    the ISKWN ZC OYNIGYFO QZTe the QSPN OeQSD
    the YKNZQeKBe ZC ZCCYBe SKO the NIUGKN
    thSt IStYeKt JeGYt ZC thUKPZGthD tSXeN
    PheK he hYJNeQC JYWht hYN HUYetUN JSXe
    PYth S MSGe MZOXYK PhZ PZUQO CSGOeQN MeSG
    tZ WGUKt SKO NPeSt UKOeG S PeSGD QYCe
    MUt thSt the OGeSO ZC NZJethYKW SCteG OeSth
    the UKOYNBZTeGeO BZUKtGD CGZJ PhZNe MZUGK
    KZ tGSTeQQeG GetUGKN IUFFQeN the PYQQ
    SKO JSXeN UN GStheG MeSG thZNe YQQN Pe hSTe
    thSK CQD tZ ZtheGN thSt Pe XKZP KZt ZC
    thUN BZKNBYeKBe OZth JSXe BZPSGON ZC UN SQQ
    SKO thUN the KStYTe hUe ZC GeNZQUtYZK
    YN NYBXQYeO ZeG PYth the ISQe BSNt ZC thZUWht
    SKO eKteGIGYNeN ZC WGeSt IYth SKO JZJeKt
    PYth thYN GeWSGO theYG BUGGeKtN tUGK SPGD
    SKO QZNe the KSJe ZC SBtYZK

we've also got this 'tZ' word appearing quite often. there's really only one two
letter word that starts with 't', and it's 'to', so we can be pretty sure that
'Z' maps to 'o'.

    to Me oG Kot to Me thSt YN the HUeNtYoK
    PhetheG tYN KoMQeG YK the JYKO to NUCCeG
    the NQYKWN SKO SGGoPN oC oUtGSWeoUN CoGtUKe
    oG to tSXe SGJN SWSYKNt S NeS oC tGoUMQeN
    SKO MD oIIoNYKW eKO theJ to OYeto NQeeI
    Ko JoGe SKO MD S NQeeI to NSD Pe eKO
    the heSGtSBhe SKO the thoUNSKO KStUGSQ NhoBXN
    thSt CQeNh YN heYG to tYN S BoKNUJJStYoK
    OeToUtQD to Me PYNhO to OYe to NQeeI
    to NQeeI IeGBhSKBe to OGeSJSD theGeN the GUM
    CoG YK thSt NQeeI oC OeSth PhSt OGeSJN JSD BoJe
    PheK Pe hSTe NhUCCQeO oCC thYN JoGtSQ BoYQ
    JUNt WYTe UN ISUNetheGeN the GeNIeBt
    thSt JSXeN BSQSJYtD oC No QoKW QYCe
    CoG Pho PoUQO MeSG the PhYIN SKO NBoGKN oC tYJe
    thoIIGeNNoGN PGoKW the IGoUO JSKN BoKtUJeQD
    the ISKWN oC OYNIGYFO QoTe the QSPN OeQSD
    the YKNoQeKBe oC oCCYBe SKO the NIUGKN
    thSt IStYeKt JeGYt oC thUKPoGthD tSXeN
    PheK he hYJNeQC JYWht hYN HUYetUN JSXe
    PYth S MSGe MoOXYK Pho PoUQO CSGOeQN MeSG
    to WGUKt SKO NPeSt UKOeG S PeSGD QYCe
    MUt thSt the OGeSO oC NoJethYKW SCteG OeSth
    the UKOYNBoTeGeO BoUKtGD CGoJ PhoNe MoUGK
    Ko tGSTeQQeG GetUGKN IUFFQeN the PYQQ
    SKO JSXeN UN GStheG MeSG thoNe YQQN Pe hSTe
    thSK CQD to otheGN thSt Pe XKoP Kot oC
    thUN BoKNBYeKBe Ooth JSXe BoPSGON oC UN SQQ
    SKO thUN the KStYTe hUe oC GeNoQUtYoK
    YN NYBXQYeO oeG PYth the ISQe BSNt oC thoUWht
    SKO eKteGIGYNeN oC WGeSt IYth SKO JoJeKt
    PYth thYN GeWSGO theYG BUGGeKtN tUGK SPGD
    SKO QoNe the KSJe oC SBtYoK

you might be able to figure out where i got this original message from just from
this, but let's keep going anyways. in the first line we have this 'thSt' word.
there's only one four letter word that that could be, and it's 'that', so 'S'
must be 'a'.

    to Me oG Kot to Me that YN the HUeNtYoK
    PhetheG tYN KoMQeG YK the JYKO to NUCCeG
    the NQYKWN aKO aGGoPN oC oUtGaWeoUN CoGtUKe
    oG to taXe aGJN aWaYKNt a Nea oC tGoUMQeN
    aKO MD oIIoNYKW eKO theJ to OYeto NQeeI
    Ko JoGe aKO MD a NQeeI to NaD Pe eKO
    the heaGtaBhe aKO the thoUNaKO KatUGaQ NhoBXN
    that CQeNh YN heYG to tYN a BoKNUJJatYoK
    OeToUtQD to Me PYNhO to OYe to NQeeI
    to NQeeI IeGBhaKBe to OGeaJaD theGeN the GUM
    CoG YK that NQeeI oC Oeath Phat OGeaJN JaD BoJe
    PheK Pe haTe NhUCCQeO oCC thYN JoGtaQ BoYQ
    JUNt WYTe UN IaUNetheGeN the GeNIeBt
    that JaXeN BaQaJYtD oC No QoKW QYCe
    CoG Pho PoUQO MeaG the PhYIN aKO NBoGKN oC tYJe
    thoIIGeNNoGN PGoKW the IGoUO JaKN BoKtUJeQD
    the IaKWN oC OYNIGYFO QoTe the QaPN OeQaD
    the YKNoQeKBe oC oCCYBe aKO the NIUGKN
    that IatYeKt JeGYt oC thUKPoGthD taXeN
    PheK he hYJNeQC JYWht hYN HUYetUN JaXe
    PYth a MaGe MoOXYK Pho PoUQO CaGOeQN MeaG
    to WGUKt aKO NPeat UKOeG a PeaGD QYCe
    MUt that the OGeaO oC NoJethYKW aCteG Oeath
    the UKOYNBoTeGeO BoUKtGD CGoJ PhoNe MoUGK
    Ko tGaTeQQeG GetUGKN IUFFQeN the PYQQ
    aKO JaXeN UN GatheG MeaG thoNe YQQN Pe haTe
    thaK CQD to otheGN that Pe XKoP Kot oC
    thUN BoKNBYeKBe Ooth JaXe BoPaGON oC UN aQQ
    aKO thUN the KatYTe hUe oC GeNoQUtYoK
    YN NYBXQYeO oeG PYth the IaQe BaNt oC thoUWht
    aKO eKteGIGYNeN oC WGeat IYth aKO JoJeKt
    PYth thYN GeWaGO theYG BUGGeKtN tUGK aPGD
    aKO QoNe the KaJe oC aBtYoK

now we've got 12 instances of this 'aKO' word. that's probably 'and', so we know
that 'K' and 'O' map to 'n' and 'd'.

    to Me oG not to Me that YN the HUeNtYon
    PhetheG tYN noMQeG Yn the JYnd to NUCCeG
    the NQYnWN and aGGoPN oC oUtGaWeoUN CoGtUne
    oG to taXe aGJN aWaYnNt a Nea oC tGoUMQeN
    and MD oIIoNYnW end theJ to dYeto NQeeI
    no JoGe and MD a NQeeI to NaD Pe end
    the heaGtaBhe and the thoUNand natUGaQ NhoBXN
    that CQeNh YN heYG to tYN a BonNUJJatYon
    deToUtQD to Me PYNhd to dYe to NQeeI
    to NQeeI IeGBhanBe to dGeaJaD theGeN the GUM
    CoG Yn that NQeeI oC death Phat dGeaJN JaD BoJe
    Phen Pe haTe NhUCCQed oCC thYN JoGtaQ BoYQ
    JUNt WYTe UN IaUNetheGeN the GeNIeBt
    that JaXeN BaQaJYtD oC No QonW QYCe
    CoG Pho PoUQd MeaG the PhYIN and NBoGnN oC tYJe
    thoIIGeNNoGN PGonW the IGoUd JanN BontUJeQD
    the IanWN oC dYNIGYFd QoTe the QaPN deQaD
    the YnNoQenBe oC oCCYBe and the NIUGnN
    that IatYent JeGYt oC thUnPoGthD taXeN
    Phen he hYJNeQC JYWht hYN HUYetUN JaXe
    PYth a MaGe ModXYn Pho PoUQd CaGdeQN MeaG
    to WGUnt and NPeat UndeG a PeaGD QYCe
    MUt that the dGead oC NoJethYnW aCteG death
    the UndYNBoTeGed BoUntGD CGoJ PhoNe MoUGn
    no tGaTeQQeG GetUGnN IUFFQeN the PYQQ
    and JaXeN UN GatheG MeaG thoNe YQQN Pe haTe
    than CQD to otheGN that Pe XnoP not oC
    thUN BonNBYenBe doth JaXe BoPaGdN oC UN aQQ
    and thUN the natYTe hUe oC GeNoQUtYon
    YN NYBXQYed oeG PYth the IaQe BaNt oC thoUWht
    and enteGIGYNeN oC WGeat IYth and JoJent
    PYth thYN GeWaGd theYG BUGGentN tUGn aPGD
    and QoNe the naJe oC aBtYon

there's a bunch of words that we can get for free now. 'dGead' is probably
'dread', 'thoNe' is probably 'those', and 'thoUWht' is probably 'thought'.

    to Me or not to Me that Ys the HuestYon
    Phether tYs noMQer Yn the JYnd to suCCer
    the sQYngs and arroPs oC outrageous Cortune
    or to taXe arJs agaYnst a sea oC trouMQes
    and MD oIIosYng end theJ to dYeto sQeeI
    no Jore and MD a sQeeI to saD Pe end
    the heartaBhe and the thousand naturaQ shoBXs
    that CQesh Ys heYr to tYs a BonsuJJatYon
    deToutQD to Me PYshd to dYe to sQeeI
    to sQeeI IerBhanBe to dreaJaD theres the ruM
    Cor Yn that sQeeI oC death Phat dreaJs JaD BoJe
    Phen Pe haTe shuCCQed oCC thYs JortaQ BoYQ
    Just gYTe us Iausetheres the resIeBt
    that JaXes BaQaJYtD oC so Qong QYCe
    Cor Pho PouQd Mear the PhYIs and sBorns oC tYJe
    thoIIressors Prong the Iroud Jans BontuJeQD
    the Iangs oC dYsIrYFd QoTe the QaPs deQaD
    the YnsoQenBe oC oCCYBe and the sIurns
    that IatYent JerYt oC thunPorthD taXes
    Phen he hYJseQC JYght hYs HuYetus JaXe
    PYth a Mare ModXYn Pho PouQd CardeQs Mear
    to grunt and sPeat under a PearD QYCe
    Mut that the dread oC soJethYng aCter death
    the undYsBoTered BountrD CroJ Phose Mourn
    no traTeQQer returns IuFFQes the PYQQ
    and JaXes us rather Mear those YQQs Pe haTe
    than CQD to others that Pe XnoP not oC
    thus BonsBYenBe doth JaXe BoPards oC us aQQ
    and thus the natYTe hue oC resoQutYon
    Ys sYBXQYed oer PYth the IaQe Bast oC thought
    and enterIrYses oC great IYth and JoJent
    PYth thYs regard theYr Burrents turn aPrD
    and Qose the naJe oC aBtYon

if you read the first line again then it's probably very, very obvious where
this is going, but let's just pretend that it's not and continue naively.
'arroPs' is 'arrows', 'theJ' is either 'they' or 'them' (we've already
eliminated 'then' and 'thee'), but in context 'them' seems more accurate.
'aCter' is 'after', 'Mut' is 'but' (obtained through context), 'Ys' is 'is'
(also context), 'HuestYon' is 'question', and so on. i've gone through the rest
of the text making all of the obvious changes to get this:

    to be or not to be that is the question
    whether tis nobler in the mind to suffer
    the slings and arrows of outrageous fortune
    or to take arms against a sea of troubles
    and by opposing end them to dieto sleep
    no more and by a sleep to say we end
    the heartache and the thousand natural shocks
    that flesh is heir to tis a consummation
    devoutly to be wishd to die to sleep
    to sleep perchance to dreamay theres the rub
    for in that sleep of death what dreams may come
    when we have shuffled off this mortal coil
    must give us pausetheres the respect
    that makes calamity of so long life
    for who would bear the whips and scorns of time
    thoppressors wrong the proud mans contumely
    the pangs of disprizd love the laws delay
    the insolence of office and the spurns
    that patient merit of thunworthy takes
    when he himself might his quietus make
    with a bare bodkin who would fardels bear
    to grunt and sweat under a weary life
    but that the dread of something after death
    the undiscovered country from whose bourn
    no traveller returns puzzles the will
    and makes us rather bear those ills we have
    than fly to others that we know not of
    thus conscience doth make cowards of us all
    and thus the native hue of resolution
    is sicklied oer with the pale cast of thought
    and enterprises of great pith and moment
    with this regard their currents turn awry
    and lose the name of action

i'm going to be honest, i didn't realize that i'd messed up the spacing on some
of the words in the original encrypted message (see: 'dieto', 'pausestheres',
and so on), but the general principle worked, we decrypted this message without
knowing the key.

we've just decrypted this message using "frequency analysis". we looked at the
most common letters, bigrams, and words, and worked from there. this wouldn't be
jb crypto without a lot of math, though, so let's dig a little deeper.

when we're encrypting a message, our goal is to make the encrypted message
indistinguishable from random data to anybody that doesn't have the key. this is
because if the data _wasn't_ random, then some pattern from the original data
must be contained within the new data. in this case, it was the frequency and
spacing of words, but it could be a whole bunch of other really mathematical
ideas that i really don't want to get into right now.

random data is random because of its entropy. there are a million different
equivalent ways to think about entropy, but in cryptography i like to think of
it as a measure of uncertainty.

i've just flipped a coin. did it land heads or tails? the correct answer is "i
don't know". i've just flipped 10 coins. how did each one land? the corrent
answer is "i know even less". we can quantify this uncertainty using entropy. a
single coin flip has 2 possible options - heads and tails - so we say that it
has 1 bit of entropy. 10 coin flips has 1024 possible outcomes, so we say that
we have 10 bits of entropy. the number of bits of entropy is the log base 2 of
the number of possible outcomes[^weighted-average], i.e. the number of coins
that you flip.

[^weighted-average]: technically it's a weighted average of the log base 2 of
the probability of each discrete outcome, but this is a lot simpler.

since there are 26 letters in the english alphabet, it'd make sense for each
letter to have 4.7 bits of entropy (log\_2(26)), but that's not right. to show
what i mean, try to fill in the blanks for this sentence:

> the establ\_shment doesn't do sh\_t

there are two missing letters, so there should be 9.4 bits of entropy, which
would mean that there are 676 equally likely outcomes, but only one of those 676
outcomes actually sounds reasonable: "the establishment doesn't do shit".

with true random data, each letter has 4.7 bits of entropy. that is to say that
it's impossible to guess some random letter with an accuracy of more than 1/26.
any decent crypto system will "diffuse" entropy around an entire text in order
to create fake entropy. that means that if i change a single letter of my
plaintext, the entire ciphertext changes. for example, if the first line of the
soliloquy read "to be or not to bb that is the question", then the entire
ciphertext would change. this effectively means that every character has the
same amount of entropy, and that the only way to figure out the original message
would be to just guess every possible message.

diffusion is always paired with confusion. the difference is that while
diffusion spreads the entropy of the text, confusion spreads the entropy of the
key. by the way, [confusion and
diffusion](https://en.wikipedia.org/wiki/Confusion_and_diffusion) were first
discussed by Claude Shannon in _A Mathematical Theory of Cryptography_. he
basically invented modern cryptography, information theory, digital circuits,
and a whole bunch of other stuff.

that's all i have to say for now, stay tuned for part 5 where i discuss some
actual block ciphers.
