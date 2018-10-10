(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('南安市', {"type":"FeatureCollection","features":[{"type":"Feature","id":"350583","properties":{"name":"南安市","cp":[118.386279,24.960385],"childNum":4},"geometry":{"type":"MultiPolygon","coordinates":[["@@@@@@@@B@@@@@@@@A@@@@@@@@@@@@@@@@@@A@@@@@@@@@@B@@@@"],["@@@B@@@B@@@@B@@@@@@@@@BA@@@@@@A@@@@@A@@A@@"],["@@@@@B@@@@@B@@@@@@@@B@@@B@@BB@@A@@@@@A@@@A@@A@@@@@A@@A@@A@@B@@"],["@@GEGCICUKAAEASBI@AB@FAJCD@@AB@@A@AA@@@@ABA@ABCB@B@@AB@@@@@@A@@B@@@@@@@@@@@@@B@@@BA@@@@@@B@@@@@B@@@@@@@@@@@B@@@@BB@B@@@D@@@@@B@@@@@@@BBB@@ABBB@B@@AB@@@@@@CCB@A@@A@A@@@@@AA@@A@@A@@A@@A@@@AA@@@@AA@B@A@@AA@@A@A@@@@@CBA@ABB@A@@B@B@@@@@@@@@B@B@BBB@@@B@@BBB@BB@AB@BABB@@@BA@@B@@@@BBB@@B@@@@@B@BBBA@AD@@@@@B@@@BB@B@@AB@B@@@@@@@BB@@@@BAD@@@@@@@BA@DB@@@@B@@@B@@@@@BA@@B@@AB@@B@@BB@@B@@@BB@@BB@@B@@@B@BBB@@AD@@AB@BA@@B@@@@@B@B@@@B@@@@CD@BABDBB@@BBB@@BB@@@BB@B@@@BBB@BB@B@@@BAB@@@B@D@B@@@D@B@BBBBD@@ABA@@B@@AB@@A@CB@@@B@@@BA@A@AB@@A@@@ABA@@BABAC@@AB@B@@@BA@@@@B@B@@@B@@@@DBBB@@@B@B@@@BA@A@@@@@@@@@@@AB@@@B@@A@@AAA@B@B@@A@@@@@@B@@A@@@A@@BAAA@@BA@@BAD@@AB@@@AA@@@A@@BA@@@A@@@@B@BA@@@@@AB@@@@@B@@ABA@BF@@BB@@B@@@@@@@BB@@BD@@BB@@@@@BBBBB@B@@AB@@B@D@@@@@@B@@@B@B@@@B@@@BB@@@B@@BB@@@@B@BB@@@@@@@@@B@@BB@@@@@BB@B@@@@@@@@BB@@BB@@@BBB@@@@ABE@@@@B@@A@@@@B@@@B@@@@B@@B@@@BABABAA@BA@@@B@@@@@@BAB@@A@@@A@A@AC@@AB@@@BA@@@A@AA@A@@@@@AA@@B@@@@@B@@A@@@@@@@@@@BB@@@BB@@@@@B@@@@@BA@@@@@A@@@A@AA@B@@B@@B@@B@@@@@@B@@A@@BA@CB@@@BBBB@@@@@@B@B@@@B@@@@@A@@A@@@AB@@@BA@@BA@AD@@@@@@@@BB@@@@@B@@@@@@@@@BB@@@B@@@@BB@@@B@D@BA@@@@B@@@@@@BB@@@@@@@@BBA@B@@@@@@@@B@@@@@@BB@@@@@BB@@@@@A@AB@BABA@A@@BBFB@B@@@@AB@@@@BB@@@B@@@D@@@B@BBBB@BB@@AB@@@@B@@@@@B@@@BB@@A@A@ABA@@B@BAD@@AB@@@BB@B@@@@BBBBB@BBA@@B@@@B@@@@A@@@@@@A@@@@@@@B@@A@@B@@@@A@@@@B@@A@@B@@@@@B@@@@B@@B@@B@@@@A@@AA@@@@B@@@@@@A@@BB@@@B@@@@@AB@@CB@BB@@@B@B@@@@@B@@@@@@@AB@@A@@B@BA@@BB@AB@@@@@B@@A@@@A@A@A@A@@@A@@@@B@AAA@@@AACBACAABCBA@@BA@@@AB@@@B@@A@@@A@@@AB@@@@A@@@@@@BAB@BA@A@BB@@B@DB@@@BBB@@@BABB@BB@@@@@@B@@@AB@BA@A@CB@B@B@@BB@@BD@@A@A@AB@@A@@@C@AB@@@B@@@D@@@@ABABAB@BA@A@CB@@EBAB@@BD@@@@AB@@AB@@@@A@ABABA@@@@@AAABB@AB@@ABA@B@@BB@BD@@@B@@BB@B@@@B@@@B@@A@@@A@@@@@A@@BCB@@A@@BA@@@@BA@A@@@A@A@A@AB@@AC@@A@A@@@A@@B@@@B@@@@@BCBA@@BA@A@@@AA@@@@A@@@A@@@AA@@A@AAA@@@AB@@AB@@@AA@@AA@A@@@AA@@@@@AAA@@AA@@@@@@AA@@@@@AA@@@@@@@@B@@A@@@A@@AA@A@@BA@@BA@@BAB@B@@AAAA@@AA@@A@@@A@BB@@@@AB@B@BA@@BA@@BA@A@@@@@A@@@@AA@AA@@A@AAB@AA@@@A@@@@@A@@@A@@A@@@@@@A@@@@A@@@@@@@@@@@A@AA@@@@A@@A@@@@C@A@CB@@ABA@A@@@@@@B@B@@@B@@ABA@A@@@DB@BA@@B@@AB@@ABA@@B@@@@AB@@AB@@@@@BAB@@@BA@@B@BB@@BABB@@@@@B@B@@@BB@@ABAB@@AB@B@@BB@@B@@B@@@@@@@@AB@@@@A@@@@BA@@A@@A@@BA@@@AB@@@@@@A@@@@BA@@@AB@@@@A@A@@@AB@B@@@B@@A@@@C@@@CD@@@BA@@DABCA@@@@A@@A@@AB@B@@A@ABCB@@@@ABA@A@@@ABAB@@ABAB@@AB@@BB@BB@BD@B@@@@BB@@B@@BB@@B@B@@BBB@B@B@D@AB@@AD@BA@AB@@ABAB@B@@@@@@@BA@A@@BAB@B@@A@A@@AA@@@CA@B@@A@@B@@CAA@ABA@@BA@@@@@A@@@@@AC@@A@A@C@@@A@AB@B@B@@CBABCB@@AAA@@@A@A@@@@@A@@@@@A@A@@@A@@@AB@@CACA@@ACAA@@@D@F@@@BA@EDABA@@@@B@@BB@@AB@BB@AB@@CB@B@@@@@B@@@@A@@@A@@BA@@D@@AB@@ABA@A@@@@@C@A@@@A@@@A@AB@@@@@@BB@B@@BBAB@@BB@@DDA@@D@@@@@B@@BB@B@BABCBB@AB@@A@@@@@@J@@@BBBB@@B@B@BB@BBAB@@@BB@BB@@B@@@@@BB@@@B@@@B@BB@@@@@AD@B@@AB@@@B@@@@A@@@BBB@BB@@@B@B@DBF@B@B@BBB@B@B@@@@@B@@A@@B@BA@@B@@@BB@@@@B@@@B@@B@@@@@@@BB@BB@@@B@B@B@@@@@@B@B@@@@@B@BA@@B@@@@@BB@A@@B@@A@@BA@@B@@@B@@@@@BBBDF@B@B@B@B@BAB@B@@@B@@@B@B@@@BA@@B@BA@@@AB@@@B@@B@DD@@B@@BB@@ABAB@B@DAD@@AD@@AD@BAB@B@@@B@B@B@BB@@@@@BBBBBBB@@B@@AB@@@B@B@@@D@@@@BB@@BBB@B@B@@BB@@@@@@BB@@@A@@@@@@BABADABABA@@D@BAB@FAB@@@@A@ABA@A@@@@@@B@@@DC@@B@B@@@DBBBBB@@BBFFBCB@BAB@B@BAB@B@BA@@B@B@B@B@B@@BB@@BBB@@@@@@@ADA@@B@B@@ABA@@BA@@B@@@B@B@@@B@@@B@@@B@@AB@@@@@@AD@@@B@@@@@B@@@B@@@@@B@@@B@@@@@@A@@B@B@@@B@@@@@B@B@@BB@@@@BB@@A@@BBB@BA@@BA@@B@@B@@BA@@B@B@@@@@A@@A@@BA@@B@B@@@@@B@@@B@AB@@@@B@@@B@@@B@B@@A@@@@A@@@@@@@B@@@@A@@A@@@@A@@B@@@@A@@@@B@@BB@BBBD@@BFBBBB@@@B@@@B@B@B@B@B@B@@B@B@D@D@B@BB@@@B@@AB@BABGF@BABCDABA@@BCBAB@@@@@@AB@B@B@BBBBBBBBB@@@BAB@@B@B@B@DA@@DF@BDD@@@B@@@BBB@B@B@@D@@BABBB@@@B@@@BABA@B@@B@BBBDDBBBB@@@@@@@@@B@@@@@B@@@BB@@@@@@B@ABB@@@@B@A@BBDABAB@@@@@@D@B@@@BBBBB@@B@B@@DBBBB@BBBB@@@ABABAB@@AA@@C@@AA@@@@AA@@@A@C@AA@@@@A@@@@@ABAB@@A@CA@@@AA@A@A@ABAA@A@@@@A@AB@@AB@@AB@@C@@BA@@@@@A@@BAA@@A@@@@@@@@@@B@@B@@@@@BB@@@@@B@@@BB@@@@@AB@@ABC@@@@@AA@@A@AAA@A@@@@@B@@AAA@@@@A@@@@AA@@@AA@@@A@@A@A@@BA@@BA@@@ABABAB@@A@A@A@@BA@@@@D@@@B@@AB@@@BAA@BA@ABBBAB@BA@@@A@A@A@A@ABA@AB@@A@@@A@@@@@@@@@@@@@@B@@@@ABBBA@@BABA@@BA@@B@B@DA@@@@BA@@D@B@B@BBB@BBB@B@B@B@B@@BB@B@@@B@@@@@D@B@D@BABBB@@@@BB@@@@@BB@B@BBD@BBDBD@B@B@@@@@@B@BE@@@@DDH@B@@@@A@@@ABB@@@AB@@A@@BAB@@AB@@@@@BB@@@@@@BC@@BA@AA@@@@A@@@AD@@A@@B@@AA@BAA@@@B@@@B@B@@@@BBBB@BABA@@@A@A@@@A@@@@AA@@@A@@@@@A@@@@@A@@@@B@BA@A@@B@B@B@@@@A@@@@@A@@BAD@@B@AB@@@@CA@@@@@BBBA@@@A@A@@AA@@@@BA@A@@@ABE@@@A@A@A@@@A@@@A@A@@@@@A@@@A@@@@@AA@@@@A@A@A@@@@@A@@@ABCBAB@@@@A@@@@@@@A@A@AC@@@A@@ABA@AB@B@BAA@@AA@@@@A@@AAB@@@@BB@@A@@@@@@BA@@B@@@@BB@@AB@@@BC@@@@@@B@@@@@BAA@@A@@@@B@BBBA@A@@@@B@@A@AAA@@@ABA@AD@@A@@@A@@B@@@B@@A@@@@B@@@@D@@@@@@B@@@@A@@B@@@@@B@B@@CAA@@A@@AAB@AAEDAB@@@BBB@@BB@B@@@@B@@@@BBB@@A@ABABBB@B@@AB@@B@ABB@@@@@BBB@@@@AB@BB@@B@BBB@@B@@BB@B@BBB@@@@BB@@@@B@B@@@@B@@@@A@@B@BB@@@@@@B@@B@@@@B@@B@@B@@B@@@AB@@A@@@A@A@@B@@A@@@@@BB@@@@A@@@A@A@@@@BA@AA@@@@A@@B@@@@@@AB@@@@B@@B@@@@A@@@A@@B@@A@@@@@A@@@C@@@@@@BA@@@ABABAB@@A@@@@B@@@BABAB@@A@C@@@@BA@ABB@@BB@@BB@@B@@@@AB@@@DAB@@@B@@@BAB@@@@@B@@@B@@@BB@@B@@BB@BB@@B@@@@BA@@B@B@B@@BB@@@@B@BAB@@AB@@@B@BB@@B@BA@B@@B@@@B@@@B@@B@BBDB@@@@@BA@@@@@@@A@@@@BA@@@@@@@B@@@@@@@ABB@@@@@B@@BA@@AA@A@@@@B@@B@@@@BBABB@@A@@@@@@@@BB@@@BBA@BBB@BAB@D@@AB@@B@@B@@B@@B@B@@@@@FBBBB@@@@@@AA@@AA@@@BA@@BABA@@AA@A@A@@@ABA@@@@@A@AAA@@AA@@@@A@@A@@@@@A@@@@@@@A@@B@@A@@B@@@@@BB@BB@B@@@@@@A@@@@@A@@BA@@@@@A@@BB@@@ABAA@A@@@BA@AC@@@@@@@@@@A@@@@A@@A@@A@@A@@@@@@BA@@AA@@@@AA@@@A@@@@D@B@@@B@@A@@@@@AB@@A@@@@@A@@B@@A@@@A@@@A@@B@BA@@@AB@B@@@@AB@@@B@@@BABA@@B@@@B@@@@A@@@@F@DA@@@A@@@AB@B@@@D@@@B@@@B@@@BA@A@@B@@@B@@@@@B@@BB@@BB@@@FA@B@@@@BB@BB@@BB@@BB@B@DBB@@B@@@@BD@@@@@@BA@@B@@@@AB@@@@@@BB@BBBBB@B@@@ABAD@@@@BBB@@BB@B@B@@@@@B@@@@@B@B@@@@@@AAA@AHA@@B@@@BBBB@@DA@@@@B@@@B@@@@@@@BA@@@@@@@@B@@@@@@AB@A@CC@@CC@@@@B@@@B@B@D@@AB@B@B@B@@@B@@A@@@@B@@AB@@@BB@@BAD@@@B@@AB@B@@@@AB@@@BA@@B@@@BDB@@BB@B@B@@@@@@@AD@BB@@BB@@@@@B@B@@@@@@@AB@@@@A@@@@@@@AB@@@@B@B@@@@DBB@A@@@@BA@@@@@@@@B@@A@@@B@@@@@BB@@BBA@@@B@@@@A@AB@@B@@@C@@@@@@BA@@@@@@@@@A@AB@@@@@@@@@@DB@@ABA@B@B@ABA@@@@@@B@D@@A@@@A@@@A@@AA@@@@@@A@@@@@@A@@@C@BBB@@@@@@@@B@@@@@@B@@@@@BB@ABB@@@@A@@@@@@@@@@@B@B@@B@B@@@@@BA@AB@@@@@@A@@@AB@@@@A@@@@@@@@@@@@B@@A@@B@@@@@B@@AB@@D@@A@@@AB@@@@@B@DD@@BA@@@@AA@@@@AAA@@A@@@@@@BAB@@@@@B@@@@@@AB@@@@@@@@@@@@@B@@@B@@@@@@B@@@@B@@B@@@@@@@B@@BBD@@@@A@@@@@@@@B@@@B@DA@@@A@A@C@@@AB@@@B@DA@@@@AACA@@@@@@BABC@B@B@BBB@@B@@@B@@B@@@A@A@A@@@@AAB@@@BBBB@B@@BA@@@@@BB@@@@@B@@@@@@AB@@B@@@@@B@@A@@@@@@@@BB@B@@A@@B@AB@B@@@@@B@@@B@@@BBB@B@BB@@B@@@@ABA@@@A@@@@@A@ABBB@@@@@@B@ABB@BB@BB@B@AB@B@@BBBB@@B@@@B@@@DB@@AB@@@B@@@@BB@@@@A@@@A@AA@@AB@@@@@B@BB@@BB@@@@BB@@B@BA@@@BB@@B@@B@A@@@A@@@A@@BA@A@@BA@@@@B@B@B@@@BAB@B@B@@BBB@B@@B@@@@B@@@@@BB@@B@@@B@B@@@@D@BBBAB@@@AA@@B@@AB@@A@AB@@A@A@AB@B@@@@A@AB@@@B@B@@ABA@@@@F@@@DBB@B@@@BBBB@@@@B@B@BBB@B@B@B@D@B@B@B@B@@@@@@@@A@@@ABA@A@A@@@@D@BAB@@@@@BA@@@@B@B@BA@@DBB@BA@@@@B@BA@@DBB@D@BAB@BAB@@BB@@BB@DB@@@@BB@@B@B@@B@@@B@@B@B@@@B@@@D@B@D@B@B@B@BB@@@@@@AB@@@@@@@B@@@@@BB@B@@@@@@BB@@B@B@BABB@@@@@@@@B@@@BB@B@@@@@@B@@@@B@DB@B@@BB@@BBB@@@@BB@@@B@@@@A@@BB@@@@B@@@B@@@@@@@@@@@B@@@@@@B@@@@@BB@@A@@BBB@@B@@@@B@B@@@@@B@@@@@@B@BB@@@@@@B@@@@@BB@@@A@@@@B@@@@@B@BBB@B@@@@@@@@A@@@@A@B@@@@A@@@BBB@@@BB@ABBB@@@@B@@BB@@BB@@@@@BB@@@B@@BB@@@@A@@B@B@@@@B@@@BB@@@@@@@BA@BB@@@@@B@@@@AB@@@@@@@@@@BB@@@BA@@@@B@@@B@@@@@BAB@B@@@B@B@B@B@B@@@AB@@B@@@B@@AB@@B@@@BAB@@BB@@@@@@@AB@@@B@@@B@@@B@@@B@@B@B@@B@@BBB@B@D@B@@BB@@BFB@@@@@@@@@@A@AD@@AB@@@@@B@@A@@@@@@@@B@B@@CB@@B@@@BB@@BBB@@@B@@@@B@@@@@@@BD@@@@B@@@B@@@BB@AB@BA@@@@@AB@@A@@@A@AB@@@B@@@B@@AA@@@@@@A@@B@@@@@@@@@@A@@@@@@@@B@@@@@BB@B@@B@DA@@@@@A@@AAB@@@@BB@@@@A@@BB@B@@BB@@@@DA@@BC@AB@@A@@BA@@BB@B@@@@@@@@@A@AAA@AB@@@F@B@B@@@B@B@@@@A@@@@@A@@@@BA@@@@BABA@@B@@A@@BBBB@@BD@@@@@B@B@@@BB@@@BB@B@@@B@@@BDDB@BADB@@B@B@@@B@@@@B@ABB@@B@@@@@B@B@@@@@@AB@@@@@BB@@BDB@@@@@B@@BB@@@BB@@B@@B@@BAB@BDB@BBBB@B@@B@@@B@@@@BB@@@B@@@BAB@BADA@@DCBBBB@A@A@A@@BC@AB@@AB@@@BA@@A@@@@A@ABA@A@@AA@@@@@ABBACAA@@BA@@B@B@B@@BBB@@B@@ABBB@B@BABB@@@@@A@@@A@@@AB@@@@@@@BA@@@@@AB@@@@@B@B@BDBB@@BAB@D@B@BBB@@@B@B@@AB@DBDAD@D@@@B@B@@@@@B@ACBABA@A@@AA@@A@@@@@A@@AA@@AA@@@@A@@AA@@@A@@AA@@@@@A@@BA@@AAB@@A@@@@@@@A@@@@@@@@@A@A@@@@@@@AB@@A@@@A@@@A@@B@@@@@B@AA@@@C@A@@AA@@A@@@AABA@@A@@ABA@A@A@@A@@@A@@A@@@@A@@@@A@@@@DA@@AAAA@@@@B@F@@@@AB@@@AAAA@@@@@@@@B@@@@A@AB@BADA@@@@AA@AB@@@@@@BB@@B@@@@@@BB@@@BBB@@@@BB@@B@BA@AB@@@B@B@B@@@@ABAB@AA@@@A@@BA@ABABA@@@@B@@A@@B@@ABB@@B@@@@AA@@@@A@@BA@@@@@@@@@@@C@A@A@C@@AA@AB@@A@@AA@@@A@AA@@C@A@@@AA@AA@CAA@E@@@A@@@A@@AAC@A@@@C@C@@B@AA@@A@@@@@ABA@@BAB@@@@AB@@A@@@A@@@@BCAA@@@AA@@AB@@@@@B@@@@A@@A@@@@@@ABABA@AB@@A@@B@@A@A@@AA@@@AA@A@@A@@BABA@AB@@ABC@CDC@@@A@@BA@@@@BA@A@A@@BA@AA@@@@@A@@AAABEA@@AA@@@ABA@@AA@@@@@@@A@@AB@B@BA@@@AA@AE@@@C@@A@@A@A@A@@@A@A@AAC@@@A@A@AA@AC@@A@@A@A@@@ABA@@@A@A@@@ABABA@@@A@@@A@@@A@@CC@@@AA@C@A@AAA@@A@@@A@@@@AAA@@@AAAAAA@@AA@@@AAC@A@A@AA@@A@@A@@ACB@AA@A@@@@@A@@A@@CA@A@@@A@@B@@A@@BAA@@AB@@ABA@@BAB@@A@A@@@@@C@@@@@C@C@A@A@@@C@@B@D@@@@AB@EEAA@ABADEDADBB@NK@@CG@@@A@A@@AAC@A@@@A@@AA@@@AB@@A@A@AA@@@A@A@@DBB@@@@A@A@A@@@@A@BA@A@@@A@@@@@@@A@@@@@@@AB@@AACB@B@@@BA@@@@@@B@@@BABAB@@@BBDBB@@@B@@@@CBA@A@@B@B@BA@AB@@A@@@@@A@@B@BAD@B@@A@@AA@@A@C@CCA@BABA@@@AA@@A@@@A@A@ABABA@@@@BA@@@@BAB@@A@ABA@@BA@@B@@@@@@AB@@@@C@@@A@A@A@A@@@@@@BA@AB@BABA@@@@@AA@@@@A@@@A@A@@@A@@AA@C@@@ABA@@@A@AA@@A@A@A@AAACA@@@@BC@@@A@@@AA@AAAAB@@A@A@@@@@@AAA@A@A@A@A@CA@@A@@AA@@@A@@BA@@A@@CBA@@BA@AAA@A@@@@@AA@A@AA@ABA@AA@@@@@A@@@A@A@@@@BABA@@BE@@B@@A@@@A@A@@@A@@@@@A@A@@A@@A@@AA@@AA@@C@@A@@A@@AE@BACA@@AA@@A@AA@@BA@AA@@@A@A@AA@@A@@A@@@A@@A@@A@@@@@AA@@@BAB@@AA@A@B@A@CAAAAA@@D@@A@A@@@@@@@@@A@@@AAB@AA@@@@@@@A@@AA@BAA@@@@A@@A@@AAA@@A@@@@@@A@@@@C@AA@@@@@@@EC@GBA@CBA@@@A@GD@@AAAA@A@@A@A@BAAAA@@@@AAA@A@@B@BA@@A@@@@A@@BCAAC@AA@@A@A@AAA@C@CAA@C@@@A@@A@A@@@CBA@A@@BA@@@@@A@C@@@AA@AA@@@@AC@A@@AA@A@@@@EA@@AA@@@A@@@@CAA@@@@A@ABA@AB@@@@A@@A@AA@@A@@@@@@BA@@@@@@@@B@@A@A@@@@@A@A@A@A@@@A@A@@@A@@@@AB@@@@@@@@AB@@@@@@@@A@@A@@@A@@@A@@@@@AAA@@@@@A@B@BAA@@A@@@AB@@@@AB@@A@@@A@AAA@A@A@ABC@@A@AA@@AABAAA@A@@@@AA@@ACA@@@A@@A@@@@@A@@@A@@@@@@DC@@@CBC@AB@BAB@@AD@@@AA@@@AB@@@@@@AD@@AB@@A@A@@@C@@@AAA@@AAA@@B@@AAA@@@@@@@@@@@A@AA@@@BA@AA@@A@@BA@@@@@@A@@@ABA@@@AAAAA@@@@A@@BA@A@CBA@@A@@@@@A@@@@@@A@@@@A@@@@A@@@@@A@A@A@A@@B@@AAA@@@BAAA@@@@A@@@A@@@@@A@A@@@@@A@@@@@C@@@A@@@@@A@@@A@@BA@A@@@AB@A@@@@A@@A@@@AA@BC@@BABA@@@@A@AAA@AD@@@@@@@B@@A@@@@@@@@@@@A@@A@@AB@@@@@B@@@@@@@@@B@@@@@@@B@@@@@@@B@@@@@@@@AB@@@A@@@@@A@@A@@@@AA@@BA@@@@B@@@@@@A@@@@@@B@@@@AB@@A@@AAA@@BA@@@A@@BA@@@@@@AAAA@@B@B@@@B@BA@@@@@@@C@@A@B@B@B@@@B@@AA@@@@A@A@@@AA@@@AA@@AA@@C@@@@@AA@@B@BA@@@ABA@ABABE@@@@D@@AB@@A@@@A@@@A@@AA@ABABA@A@@A@@A@A@@AA@AAA@@@A@@AAAA@A@@@AAA@@@A@@@@@@@A@@A@BC@A@AA@@@B@@@BAGG@@@@@@A@EB@@ABAB@@@@A@@@@@A@@A@@@@@AB@AA@@@A@@@@@@@AA@@@@@AA@@@@A@@A@@@AA@@AAA@@A@AAAAA@@@@AAAC@@@A@@@@A@@A@@AAAAA@A@A@AAABAB@@@DABB@@B@@@BAB@B@DA@@@BB@B@@@@@BBBB@@@BB@BAD@@@@@@@@AA@@A@@@@HEBA@@@C@@BA@AA@A@@A@@@@A@BBA@@@ABAA@@B@@A@@@@A@@@A@CA@A@@@@@@@@@@A@@A@@@@@@@AACA@AA@AB@@@@C@@@@@@B@B@BA@@B@@@@@B@@@B@@@B@BA@@@@B@B@@@@@AAB@@@BA@AA@@@@A@@@CC@@A@@D@DA@@@@B@B@B@@A@@@AA@@A@@@A@@AAAA@A@@@@@AAA@@BA@A@AB@AA@A@@AAA@BA@@@@@@BA@@BAB@@A@@BA@A@AHG@A@A@AB@BC@@@@@E@@AA@@@A@@@AB@@A@A@@BA@@B@B@@A@A@ABA@A@@A@@AAG@AAECI@E@GBKFEBIAEEGACACCMAI@C@I@@@K@I@@@E@CBA@AFOIECACCIEEEEEECC@CAGAA@GAECICAAEA"]],"encodeOffsets":[[[121270,25180]],[[121289,25160]],[[121301,25152]],[[121240,25180]]]}}],"UTF8Encoding":true});}));