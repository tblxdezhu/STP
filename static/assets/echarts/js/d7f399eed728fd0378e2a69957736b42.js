(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('长白朝鲜族自治县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"220623","properties":{"name":"长白朝鲜族自治县","cp":[128.200789,41.420018],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@A@AAA@@@@@AA@@@@A@@A@@@@@@@@@@@A@@@@@@@A@@@@@@AAA@@AA@ECA@A@A@AAC@ABA@EBCBA@ABGFCDAB@@@@A@@@AB@@G@A@@@@@A@@@@@@@@@@@@AA@@@@@AAA@@AA@CAA@ICA@A@A@A@A@A@@@AB@@A@@@@B@@@B@@BJ@B@@@B@@@B@@A@@BA@A@A@C@C@@@@@A@@AA@CA@@@@A@@@@AAA@@AA@@@A@AAA@A@C@@@A@@@A@@@AB@@ADC@@@@BA@@AA@@AA@@GCA@CAC@C@M@CBA@A@C@@BIBC@C@ABC@A@@@A@@@A@@@AAC@AA@@A@@AA@@AA@@AA@A@A@C@A@A@CBCBABEF@BA@@B@@@D@B@B@D@@@B@B@B@B@@@BA@@@@@ABAB@@A@@@A@CBA@A@EBG@@@@@A@@@C@@@A@@@CA@@AA@@@@E@AAA@A@@@A@A@E@CBG@C@A@@@A@@@A@@AA@@@@@AA@@@@@A@@@@@@@A@@BA@@@A@C@AB@@A@@AG@A@@AA@@A@A@C@A@C@A@A@CBMDA@A@@@ABC@CDA@A@@@EB@@A@@@@@ABA@A@ABCB@@CBA@CBCBA@CBCBABC@@@CB@@A@CBABEBCBE@@B@@A@@@A@AAA@C@@@@@A@@A@@A@@@@@@AA@A@A@CA@@A@@@CCAA@@A@C@E@K@A@E@ABCBC@CBABAB@BA@@B@B@@BB@@B@BBD@LDHBD@D@H@DBB@B@BBBB@@B@BDB@@BB@@@BB@@@@BB@@BB@B@@@@@B@@@@@B@@@@@B@BADAD@BA@@B@@ABA@@@ABA@@@@@A@EB@@A@E@@@A@A@A@@@EAC@@@A@@@@@A@@@@AAA@@@@@@A@@AGEGGAACAAAA@@@A@A@A@A@@BWN@@@@@B@@@@@B@@B@JH@@BB@@@BBD@B@@AB@@EDABA@C@@BBBBBB@DB@BC@C@@BAB@BA@@BABAB@B@B@@@@@B@@@B@B@@B@B@@@@@B@@AB@@@@@@@@@@@BB@D@@@B@@B@B@BBBA@@B@@@@@@A@@@AB@@A@@B@@BB@BD@@@BBB@@B@B@@@B@B@BA@@@@@@AA@@@@BA@@B@@@BAD@B@@@@@B@@@B@BBB@B@@B@@@@AB@@@BABAB@@@B@@A@@B@@@@ABB@@BB@BB@@B@B@B@B@BAB@@@B@B@B@B@@@@@DBBB@@B@@@B@@@@B@@@B@@A@@BA@A@A@A@@BA@@B@@A@@@@B@@BBBB@@@B@@B@B@BB@@B@B@@BBBB@@B@@@B@B@B@@BBB@@BB@DBB@@BB@BBDBB@BBDBD@@@BB@@@@BF@B@@B@@@@@@B@@B@BBD@@BB@@BB@BBBB@@@@@B@BBB@@@@@BB@@BB@DB@@BBB@@@B@B@B@BAB@@ABAB@BAB@B@B@@BB@@@B@B@@@B@BAB@B@@@B@B@BBB@BB@@BBBBBD@BB@BBD@B@DBB@F@B@B@@@B@@@B@@BB@B@BB@@@@B@@@@B@B@BB@@B@@@BB@B@B@@@B@@@BB@@B@@AB@@@B@@@B@@BB@@BB@@@@BB@@BB@@BB@@@@B@@@B@@AB@B@@BB@@@BB@BBB@B@D@@@B@@@@@BD@@B@@BB@B@B@BAB@D@B@B@B@B@@@@B@@B@@B@@BB@@BBB@B@@@B@@@DBB@@BB@@B@@@@@BB@B@B@@AB@@AB@@AB@B@B@@@B@BA@@B@@@BBB@@@B@@@B@@@B@B@B@B@B@BBBBD@@@B@@@BBB@B@@@@B@@@B@@AB@@@BB@@@@@B@@AB@@@@@@@BAB@BAB@@A@A@A@@@@@AB@@@BBB@BA@@B@B@B@@@@B@@@BB@B@D@B@B@BBB@BBB@@@B@@@B@BA@@BA@@@@B@B@BBB@@@B@@B@@A@@@ABA@A@AB@AA@A@ABA@AB@@@BA@B@@@@BD@DBB@@@B@B@@@B@B@@BB@@B@@BB@@B@@@F@@@B@@@B@D@D@B@BBB@@BB@@B@@@BABABCDA@A@@@@B@@@@@B@BB@BBB@B@@@B@BA@@@ABA@@BAB@B@B@B@D@BBB@@@B@@BB@BBBBB@@B@@B@B@B@@AB@@@BA@@B@@AB@@@B@BAB@B@B@B@@@BBBBBB@B@@@BB@@@@BB@@B@@B@@@B@@BDBB@@BBBB@B@B@@@B@B@@BB@BBBBB@@@BB@@B@BA@@B@BA@@@A@@@A@A@A@@@@@@B@@@@@@@B@B@@@B@B@BBB@B@@@B@@@F@@@@A@@B@@@@@B@@@@@B@@@@@@@B@@B@@B@@@B@@@@BB@@@@B@@@@@@BB@@@@B@@B@@@@@BB@@B@@@@B@BBB@B@@@@@B@@B@@@@@@@BB@@@@@B@@@@@@@B@@@@@B@@A@@BA@@@@@@@@B@@@@@@@B@@@@@B@@@@@@@@A@@B@@AB@@@@A@@B@@AB@@@@@B@@@@@@AB@@BB@@@@@@@B@@@@B@@B@@BB@@@@@BA@@@@B@B@D@B@@AB@B@@A@@@@B@@@BB@@B@@@B@@@@AB@@@@@@A@@@@B@B@BA@@BAB@@@@@B@@@@@@A@@@@@@B@@@@B@@@@@@BB@@@@@@B@@@@B@@@@@@@@B@@@@@@@@@@@BB@@@@B@@@@@B@@B@@A@@@@@B@@@@@@@B@@@B@B@B@@ADB@@BA@@@BB@@@@BDBDBD@@@B@@@B@@@BB@@DBB@@@B@B@@BB@@@B@BB@@BB@@DB@BBB@@BB@BBBBB@BB@BB@@BBD@D@DABAB@D@BBB@D@BBDBBBB@B@FBB@B@@@@AB@BA@@B@BAD@B@D@D@B@D@D@F@B@B@B@B@@@D@B@B@B@B@@AB@B@B@DAD@B@@@BBB@B@FBB@@@B@@@BBB@@@@@B@@@@@B@BA@BB@@@B@@AD@B@BAB@@@B@B@@@B@@@B@B@@@D@BAB@B@@@BBJ@B@B@@@BA@@B@B@@@B@B@@@B@@@B@BBB@@@B@@@B@B@D@DAF@DAD@@@B@B@@B@@B@@BB@@@@@B@@BD@B@DBBB@@B@@@BBB@B@@BB@DBDBB@BBBBDDBBB@BBB@B@B@@BF@B@BB@@B@@@B@@@@@@@B@@@@@B@@@@@@@@BB@@@@@@@B@@B@@@@@@@@@B@@@@@@B@@@@@@@B@@B@@@@@@@@B@@@@@@@@@BBDBBBD@BBD@D@FBD@F@D@H@B@B@DBB@B@BBF@@BB@BBBBDDBBBBBBBDBB@BDB@@BBFDFDDBB@BBB@@BBBFFDDDBBBDBBBB@@@@@B@@B@B@DBBB@BDBDBD@B@@B@B@F@B@J@D@F@D@B@BA@@BC@ADAB@D@B@BBB@@@DCFABAD@@@B@@@@ABABAB@BAB@@@BB@@DDBBDDBFBFB@@BB@@BFDBBBB@BB@B@B@BAHAF@@@D@B@B@B@B@B@B@@B@BBBBDB@BBB@B@B@@@BBBB@@BB@B@BBBBBBBBB@BBB@BBD@BBBB@@BB@BBB@BD@DBB@@AB@@EDABABABAB@@@@@@@@DBF@DBFBDBFFDDDFBB@BDD@BBBBB@@@B@BB@@BB@FBDBB@DBB@B@D@@ABD@BB@BDBBB@DBDBD@FBD@@@FBB@BBD@D@DB@BB@D@DBB@BBFBBBBBBBBBB@BAB@D@DABBB@B@B@B@BA@@B@FAB@B@B@B@@BB@BB@BBDBB@B@@BB@BBBDDDD@@BBDBBBDBB@BBBBBD@BBB@DAD@F@@@B@BBD@@BBBBD@DBDBD@BBBB@@BB@@DB@@@@BB@@EDCD@D@@CFCFADA@EFAB@BAB@@@@DDBD@BB@@B@@@BA@@B@B@@@BABABAB@BABABA@ABA@@DAB@B@BAF@@CBAB@@@B@B@@@BB@BBB@@B@BBB@@BAB@H@B@BBBBB@D@D@B@B@DAB@@ABAB@@AB@@BB@BF@D@D@DAB@BCDA@AB@B@B@@@B@B@BBDGBAB@@ABA@AD@BBB@BBB@D@B@BBBBB@BA@A@AB@BA@BDABBHBD@B@@@BA@MDBDBBVOXQFAB@@ABAJ@BA@@AE@CAS@KAA@A@CA@@A@A@ABCBS@ABC@ABA@ABABAJG@AB@@@@A@@@@CGAG@AA@@AA_@@@AAC@@@AAKCU@A@@@AAA@@@@AA@@@@AE@@@@@@@E@A@@@@BC@@B@@A@@@@B@@@@@@@@@@A@A@@@AA@@A@@@@@@@@@E@@B@BC@A@@@@AC@@@A@@@@BE@@@@@@BABAB@@A@@@@BCBC@@@A@@@@@C@@@@AACC@@A@@A@@@@@@@@BEB@@@@CBE@@BG@A@@@@@A@@@@@@DA@@@@B@B@F@@@@AB@B@@@@@@@DC@@@@B@@A@@@@B@BA@@@@@@@@B@BA@@@@@@B@@ADA@@@@@@@@BA@@@@@@@@B@@@@@B@@A@@BBB@@@B@@@@@BBB@@@@@@B@@@@@@B@B@@@@@@@@@@@@C@A@@@@B@@@@@@AD@@@@@@@BAD@@@@@@@B@@@@@@@@@@A@@@@CA@ACA@@@@@@@@@@@A@@@@@@@@@@@@BABA@@@@@@@@@@@@@@@A@@@@@@AAA@@@@@@A@@@@@@@@@@@A@E@@@@B@@@@A@@@@B@@AB@@@B@B@DA@@@@@@@@@@@A@@AA@C@@@@@@@@@@@A@@@@@C@@@@@@AA@@@@CC@@@@@@@@@C@@@@@@@@@@@@@A@@B@@@BAB@BA@@@@@@BA@@@@@A@@@@@A@A@@@A@@@@BE@C@@@@@@@AB@BABA@@@A@@DC@@@@@@@@@E@@@@@@@A@@BABADC@AB@@@BC@@@@@AB@@A@@B@@@BAB@@@@@B@@@@@@ABA@@@@@C@@@@@@@A@@@@B@@@BA@@B@BAB@@@B@B@D@B@@@B@B@@@BA@@@@BADA@@@@B@@@@@B@@@B@@BDA@@B@@@@@@@BA@A@A@@@@BA@@@@BA@@@@@@B@@AD@BADAB@BA@@@@@A@@@@AA@@@AA@@ABA@@@@@@BADA@ADA@@@ADCBA@@@@@@B@@@@@B@@@B@FBB@B@D@@@@@@@@@B@@@@@@@BCBG@@@@@@B@BA@@@@@@BA@@B@D@B@DA@@B@B@D@@@@@B@@B@BB@@@BBB@B@@@BA@@@@BA@@@@BA@@B@@@@@B@B@D@B@B@@@@@B@@@@A@@@@@AA@@A@@A@@A@@@@@@@@@A@@@@@@@@B@@@DAD@DA@@B@B@B@@@@@@@B@@@@@@@B@B@@@@@@@@A@@@@@@@@@A@A@@@@@@@A@@@@@@AA@@@@@@@@@@@A@@@@@@BA@@B@@@B@@@@@B@@@BB@@B@@@D@@@B@@@B@@@@@@@B@@@@A@@@@AA@A@@AC@@AC@@@@@@@@@A@@@@DC@@@@@A@@D@B@@@B@@@@@@@B@DB@@B@@@B@@@@@B@@@@@@@@@@@@@@A@A@@@AA@@@CCCC@@@@@A@A@A@@@@@A@@@@@@BA@@@@B@@@B@B@D@@@@@B@@@@@@@@@@@@A@@@@@@@@@@@@@A@@@@@@@@@C@@@@@@@@@A@@B@BA@@@@@A@@@@AG@@@A@@@@BA@@@@B@@@@@@@D@B@@@@@@@B@@@@@@@BA@@@A@A@@@@@A@@AACA@@@@@@@@@@@AB@@@@@@AB@@@@@B@@@B@@@@@BBBBB@@BB@@@B@B@B@B@D@@@@@B@@@@B@@B@@@@@@@B@@@BB@@@@@@B@@A@@@@@@@@@@@@@@@@AA@@@A@@A@@@@@@@@A@@@@@@@A@@@@@@@@BC@@DCBC@@@@@@@A@A@@AA@@AAA@A@A@ADA@@@A@A@@@AAAAAAAA@@@@@@@CB@@A@@BA@@B@@@B@@@DBB@BB@@DB@@B@B@@@B@@@@A@@@A@@@A@@@@AAA@AAA@@@@@@A@@@@@C@@@@@@@@BA@AB@@@@@@@B@B@@@@@@@@@B@@@B@BBB@@@@@@@@@B@@@@@@@D@B@@@@@B@@@B@@@@A@@@@B@@A@@@AA@AA@@CAAA@@@@@@@A@A@AB@@@DC@@@@@@DA@@@@@@@AB@@@@@@@@A@A@@AA@A@@AA@@@AA@@@@A@@@@BA@@@A@@@A@@@A@A@@A@AAA@@@@@@A@@@A@@@@B@@@@AB@D@@@@@@AB@@@@@@@@@@A@@@@@AA@@@@@AAA@AAA@A@A@A@@@A@@AC@AA@@@@CC@AA@CAAAA@@@AACA@@@@@A@@@@@@@AFC@@@@@@B@@@@@@@@AA@AA@@@@AAA@@@A@@@A@@@AA@@@@AA@E@@@A@@@A@@@@BA@@@@B@@AB@@@B@@@B@@@@@FC@AB@@@@A@@@A@@@A@@@@@A@A@@A@@@AAA@@AC@AAA@@@A@ABC@A@@@A@@@@@AAA@@@AA@@A@@AA@@@@@@A@@AA@@@@@@@@@@BA@@BA@@@A@@@@@A@@@@@AAA@@@AA@@@AA@@ECC@@AA@MK@@@@AA@@@@AAA@@AA@@@AC@AEC@@AA@@A@@@A@A@E@@@AA@@A@@@@@AC@@@@AA@@A@A@@@GACA@@@@EC@@@@AC@@@@AA@@@A@@BA@A@A@@B@@@DA@@B@BA@A@@@@BC@@@EAI@C@@@AA@CCAA@AA@@AAC@AA@ACCE@AAA@@@A@C@A@@@A@@BA@@@@B@BAB@@@B@B@@@H@@@B@@@B@@AB@@A@@@A@@@AA@@AAAAACAA@CAA@A@@@K@A@@@A@@@AAGCCA@A@@AAAC@@AGAA@AA@@AA@CC@@AA@@@@@A@KA@@E@A@@@A@@@@@AAA@@@AAA@@AA@AA@@@@@EA@@A@@BE@ABCBA@@@A@ABC@C@@@AAA@EAAACAICCACACAAAA@@@AA@@AAACAA@ACGA@@A@CA@@AAA@AAAAACACAAAC@OCA@@@A@@@@@A@ABC@@@A@A@A@C@C@A@@@A@@@AAA@AA@@A@@AA@@AA@@A@@@AAC@@@A@@BC@@@@@AA@@@CCGI@@@@A@@@A@@@A@A@@@EB@BA@CDCDA@@BA@@@@@ABA@A@@@@@ABA@A@A@A@@@E@ABA@@@A@@B@@@BBB@BBBBBDDB@DBBBD@NB@@BB@@@@BD@BBB@B@B@@@B@@@@AB@@ABA@AB@@ABAB@B@@A@@@C@@@A@@@@@@@@A@@@@@@BE@@@A@@@@@A@@A@@@A@A@KDA@A@C@A@A@A@AAA@AAA@@A@@@A@@@A@@DEBE@A@@@@@A@@@@@A@@A@AA@@A@@@C@A@A@@@AB@@CB@BAB@@AB@BAB@@@@@B@J@@@B@@@@@BA@@@A@ABA@CBA@AB@@A@A@A@E@A@@AA@A@GE@@A@@AE@@@A@I@A@@@A@@@ABA@@@@BA@@@@@@@@B@@@@B@@BFB@BB@@@@B@@BB@@@BA@AJAB@@@@@B@@B@@@HJ@BBB@@@B@@@@@B@@A@AB@BA@@BA@AB@@A@CBA@A@@@@@A@@A@@A@@A@A@@AA@@@AA@EEAAA@A@@@E@A@A@ABA@AB@@AB@B@@@DAB@@@BB@@BBHB@@B@@@BA@@@@BA@@@A@A@G@@@IA@@A@AB@@A@@@@BA@@B@@BB@@BBBBDBJDB@@BB@@@@BBB@@BBBB@@@B@@@@@B@@@B@B@@@@@BA@@@ABA@@@A@A@A@C@ABAAA@@@A@A@AAA@@@AA@@AAAA@AAAACCMGQ@CA@AAACA@AA@@A@A@@@AAAB@@A@@@@B@@AB@B@B@@BJ@B@B@B@B@@@B@@@@@@A@ADABA@@@ABA@CBCB@@A@CBA@A@A@A@E@A@C@IAA@A@A@CBA@ABA@A@@B@@@B@@BBFH@BBB@B@@@B@@@@A@@BA@AAGAAAA@A@@B@@A@@B@B@F@B@@@BA@@@@BA@@@ABA@A@AAA@A@@AAA@@@A@A@A@G@A@A@@@A@@AA@@AAECA@AA@@GAA@A@AAAAC@@AAA@A@@CE@A@@AA@@A@@@A@A@@@ABGHABA@@BA@A@@@AAEAAAA@A@A@@@A@ABA@ABABAB@B@@@@@B@@BBDD@@BB@@@B@@@BA@@BA@ABC@C@A@A@A@A@@AA@A@@ACC@@AAAAA@@A@A@@@A@@@A@A@@@A@C@@@A@I@A@C@E@AAC@A@A@@@ABA@ADCBA@A@A@@@A@AAA@AA@CAAAA@@@C@C@ABA@ABABCDCDAD@BABAJ@@@BA@@B@@A@CB@@@@A@C@@BA@@A@@E@IAA@A@AAA@@@AA@AA@@@@@@A@@@@@@@A@@@A@A@@@A@AB@@@@A@@@A@A@A@@@@@AA@@@A@A@@@C@A@ABA@ABABAB@@@BAB@B@D@B@@AB@@ABAB@B@@A@@BA@ABA@@@CBA@A@A@ABA@@@A@A@A@GAA@AA@@CAA@@AAA@@AA@@@A@@@@@C@C@@@@@A@@@@@@@@@A@A@@@@@A@@@A@@@@@A@@@AA@@@A@@@A@A@AB@@ABAB@B@B@B@B@H@B@B@@@B@B@B@@@@AB@@EBAB@@A@@BA@@@A@@@@@A@@@@AA@AAAAGC@AA@@@@@A@@@ABKDABCBEBA@@@A@A@@BA@@@AAC@A@E@E@C@@@@@@@A@@@@AA@@@@@A@@@@@@@A@@@AA@@@@A@@@A@AA@@C@OGCAA@C@A@O@CBC@A@MDCBIBA@A@A@A@A@A@A@AAA@AAAACECC@@AA@@A@@@A@A@@@A@AB@@A@@BAB@DA@@BADA@@B@@CBCD@@A@CB@BA@A@A@A@A@@@AAA@@@AA@A@@@A@A@A@A@@@A@@BA@AB@@AB@@@BAB@BA@@DA@@DCB@BABA@@@A@@@A@@@@AA@@CAAAC@C@C@C@EBIBIFEBABABA@ABCBAB@BA@@BA@@BA@@BABAFABCF@BA@ABABA@ABA@A@AAE@GAEAA@CAKCA@A@CAA@ABC@eHE@ABA@CBCDEDIJGHEH@BAB@@@DAB@D@F@D@H@B@@@BB@@@@@DF@@@@@B@@BD@@@B@@@@@@AB@BAB@@@@@@@@@@A@A@A@@@A@C@A@A@@@A@"],"encodeOffsets":[[130600,42473]]}}],"UTF8Encoding":true});}));