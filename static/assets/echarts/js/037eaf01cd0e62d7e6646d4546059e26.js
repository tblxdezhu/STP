(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('奉化区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"330283","properties":{"name":"奉化区","cp":[121.406997,29.655144],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@@@@@@AA@A@@A@@A@@@@AA@@@A@@A@A@@@AAA@@@@@@@A@A@AAA@AA@@A@@@A@@BA@A@@@@@A@A@A@@@@BB@@B@B@@BB@@@@@BA@@B@@@@ABA@@@@@@BAB@@A@@@@@A@@AABAB@@A@A@C@AB@@A@A@@@@@BB@@@B@@DB@B@@A@@BA@@B@B@BA@@B@B@B@B@@@@@@@B@@CD@@@@@@@@@B@@A@@BA@@@@@B@@@ABA@@BA@@@@B@@@B@@@@@@@@@BB@@@B@@@D@BB@@BB@AB@BA@@@@BBB@BB@@@B@BB@@B@@@@@@BB@@@ABBB@@@@@@@BB@B@BA@@BA@BBA@@@A@@@A@A@AAA@@@@B@@C@@B@@@BCB@@@@@BB@@@@B@@@B@@@@@BAB@@@B@D@@@BB@@BA@@@BBB@@@BB@BBB@@@@@@@B@BA@BB@@@@@B@@@BA@@B@@@@@@BB@@@@@B@@@@@@A@@AA@@B@@@@@BBB@@A@@@@BADB@B@@BB@@A@@@@B@@@@BA@@@@BB@@@@B@@B@@@@B@@B@@@@@B@@@B@@@BB@B@@BB@@@B@@@@@@BB@@@@B@B@@@@B@@@@@@@B@@@@AB@@@BA@@B@@@@ABA@A@@BA@AB@@EBA@@@AB@B@@B@@BA@@@A@@@A@@B@@@@@@@@@B@@@BB@@@B@BB@@BA@@B@B@@@B@@@@B@@B@@@@@@B@@@B@@@B@@@B@@B@@B@@B@@@@B@@@@@B@BB@BB@@@B@@BBDB@B@@@@BBB@@DA@@BA@A@@B@@ABA@@@@@AB@@@B@B@B@@@@@BA@@@@B@@@@A@@BA@BB@@@B@@BB@@@B@BBB@@B@A@@BA@@@@@@@AA@@@@A@@@AAA@@AA@@A@@@@@A@@@AABAAA@@@@AB@@AC@@BA@@@AA@@@B@@@@@BA@@B@@@@AB@@AAA@@@@@@@@@@BA@B@A@C@@@@AA@@@AB@@BB@@B@@@@@A@@@@@B@@@@BB@@@@@AB@@AB@@AB@@A@@@@A@@@@@@B@@@B@@@@A@@A@@@ABAAABABA@@@ABA@A@@@@B@@@@A@@@@BAAA@@@A@A@AA@@@A@@@@A@@@A@A@@@ABAB@@A@@BA@@@@@A@@@A@@A@@@@A@CA@@@ABA@@A@@AC@@@A@A@A@@BAA@@@@@B@@AB@@@@B@@@AB@@A@@@A@@@A@AAABA@@BA@@@@BCB@AA@AA@@@@@@AB@@@@AB@@ABEB@@A@@@AB@@A@@AA@@@A@@@AAA@@@@@ABAA@@@BA@@AA@@@@@@@A@@@AD@@@BAB@@@BBBAB@@AA@@@BA@A@A@@@AD@@AB@@ABA@@@@BAB@B@@A@A@@@@A@@@A@AA@AAEAEAAAC@@@A@@@@B@@A@@@A@ABABA@AB@@AB@B@@A@@BB@@B@B@@@B@@@B@B@B@@@@@B@B@@@BBB@@@B@@@B@@B@@@B@@BB@@@B@@B@B@B@B@@@BDB@@B@@B@@@@AB@D@@A@@@@BAB@B@B@BAB@@@B@BB@@@ABAB@@@AA@A@@AA@CA@A@@ABAD@@A@@AA@@A@@@BA@ABA@@BB@@@BB@@B@B@BBB@@@BB@@@@AB@@@@@@BB@@@@@BA@@@@BA@@@@@@BB@@B@@BB@@B@D@@@B@@BB@AB@@@DAB@BB@@@FABB@@B@@B@@@@A@A@@B@B@@A@@@@A@@A@AB@@@@@BA@AAA@@@A@@@@BA@@@@@@BB@@BBBBB@BAB@@@@@BB@@@@B@BA@CDA@@@@@A@@@A@@B@@@@@@@A@@@@A@@@@@AB@B@@BB@@@B@@@BB@@A@@BB@@@B@@@@@B@@A@@BA@@@A@@BA@@B@@A@@@A@@@A@@@@@BA@@@@ABA@@@A@@@ABA@ABA@@B@@@@@BA@@@A@AAA@@BA@@A@BAA@@CA@@A@@@A@@BAB@@@BA@A@C@@@A@@BA@A@@@@@@BA@@@@BA@A@@B@BAB@@BB@@@BABB@@@@@@@B@BB@@BB@@@@ABAB@B@B@@@B@BB@@BBB@@AB@@@BAB@@@B@@@D@@@@@B@@@@@B@BA@BBABC@AAA@@@BB@@BB@@BBBA@B@B@B@@C@A@@@@@BBA@@@CDABA@@B@@@@AB@@A@A@A@@B@B@B@@@BAB@@@@B@@BB@@BB@B@@@B@B@C@@DA@@@@BB@@BB@@@@@@B@B@B@@A@C@E@C@@B@@BBB@@BA@@B@@A@@BAABD@BA@@B@@@@B@@B@@@@@B@@BB@B@@@D@@A@B@B@B@B@BBDAD@@@@A@AA@@@@@AA@A@A@ABA@@@@BA@@B@@@@AB@B@@A@@B@BABA@A@@B@B@@@@BB@B@DB@@@@BB@@@@B@@@@BB@@@@@B@@@BA@ABAB@B@B@@@BB@@BBB@@@@B@@BBBB@@B@B@@@@@BC@A@@B@B@@AB@F@@@B@@@@A@@BABC@@AA@@BABABABA@@@@@@@@BA@@B@@AB@@@@ABA@@@@BABAB@B@@@@B@B@B@@@@@B@@@@@@AB@@BBB@BB@@@@@@A@@BB@B@@@@@@@@A@@AA@ABA@A@@BB@@@BB@BB@@B@B@@@B@@@B@DAB@@AB@@@BAB@@@@B@@BB@@A@BBA@B@BB@@@@@@B@B@@A@@B@@ADB@@@@AB@B@BAB@@@B@B@@BBA@B@@@@@BB@BAB@@A@BB@@@@@@@@@BB@@@BBB@B@B@B@B@@@@BBB@B@B@B@BD@B@B@@@@@B@B@A@@BB@@BB@@BBB@BBB@@@@@@@BCB@@@B@@@@B@BBB@@@B@BBBAB@@A@@@@@@B@DB@A@ABA@AB@@@@@BA@@@@@@@BBBB@@B@@BBBDB@@@A@@B@B@@AB@@@@@B@@DB@@@B@@@@BB@@@BA@@@@B@@BBB@@@@@AB@@@@@BB@@@@@@@BA@@@@@BB@@@B@B@B@B@@B@@@BB@@BB@A@@BB@@@@@B@@@@A@@D@B@@ABB@@B@@@B@B@BB@@@@F@@@@@@B@BBB@@BB@@AB@@AB@@BD@B@BB@AB@@@B@A@BB@@@B@B@@@DA@@B@BAB@@@@A@A@A@@BA@A@A@@@@@A@A@@AA@@B@B@B@@@B@@@BA@@@BB@@ADBDABB@@B@B@@@@@@B@@@@@@BB@BB@B@D@DBB@@BD@@@@@@A@@B@@@BA@@BA@A@@BB@@BBB@@B@@BB@@@@@@BBB@@ABA@@BADABB@@@@@@@B@@@@@BBDB@@BA@@BB@BA@@BA@@@@B@@A@ADB@@B@@B@@@B@B@B@@@@DA@@BABA@@@A@@B@@B@BD@@BB@BBBB@BB@@@D@@@BAB@@BB@BA@@@@@A@@@A@@@@@@@@AA@@@A@@B@B@B@A@@AA@@@@A@@AAB@@BB@@@BABB@@B@@@B@@@BA@@DABA@AB@@@@B@@@B@@D@D@@BB@BB@@@A@@@CBA@@@@B@@@B@BBB@@BB@B@D@@@@BB@@@BB@@B@B@@@B@B@BB@@BAB@BBB@@@B@B@D@BA@@@@B@BA@@B@@@BBB@@@B@FABAD@D@BA@@BB@@@@D@B@@@BB@@B@B@@@@B@@@@B@B@@BB@@@B@@@B@B@BD@@B@@@@@@@BABA@A@@@@@A@AB@DBBB@@@@@@BA@@@@B@@@B@B@@@B@B@@@@@@@B@@@@@@@@@@@AB@@BB@@@B@@@B@@B@DAB@BA@@ADAD@B@@B@@B@@B@@@BAB@@@B@@A@@BB@@@@BB@@B@BB@AB@BA@@B@B@@BB@ADB@@@DB@@@AB@@@B@@C@@@@BAB@B@BABBBD@@BBBA@@@@B@@@@@@@B@DC@@BA@@@@BAB@B@@@B@@@BBB@@@BB@@B@@AB@B@B@@@@@@B@@@B@B@@@@B@B@B@BBB@@@@A@@@@@A@@BB@@@@@@@@@@@@B@BAB@@B@B@B@BBADA@@@AB@@ABB@@@@@@@@@@@@ABB@@AB@@B@BA@@@A@@@A@@@CBA@@BB@@@@@B@@BBAB@@@B@BA@@@@@BC@@@ABA@@@@@@B@@B@@BB@B@B@@@@@B@B@@@@ABBB@DCB@@@B@B@B@B@@AAA@@BAB@B@B@@@B@BB@@B@@@D@DBFB@@@@BB@B@B@B@@ADAB@B@B@B@B@B@@BBB@B@B@D@B@B@@@@BB@@FAB@@A@@B@D@B@@B@@DA@@@BBBBB@@@@B@B@@@BB@BBB@D@DAD@H@D@@@@@B@BF@B@B@@@BABGBABCB@@AB@@@B@@@@BD@BB@@BB@B@BBB@B@@@@AB@B@@ABA@ADEBC@AB@@@BA@@@BB@@@BB@DBF@B@@BB@@B@B@@@B@@@@ABABA@AAAB@AA@@@AB@@@@@A@@@@@A@@@A@@@@AA@B@A@@@AA@BCCAA@@@A@@@A@@D@@CA@@AB@B@@@@A@@BA@@A@@@@@@A@@@@@A@@@@@A@@@@@@@A@@@@BA@@@@@@@@@A@AB@BB@@B@@@@@@AD@@B@@B@@@@AB@@@BA@A@@@@BC@@@@@AB@@A@@@A@ABCB@@@@@@@@@@BA@@@D@@AB@@@@@@AE@@A@A@A@A@A@A@A@C@C@A@E@C@A@E@E@ABC@CBA@A@CBA@A@A@A@ABC@@B@@AFADCD@DA@A@@@@B@B@@@B@@AD@@B@@@B@@@@B@B@@A@@@BB@@@F@@@B@@@B@D@@@@CD@BADABBJ@D@@@@ADB@@@@AHDBJH@@JC@@B@@@@@B@@A@@@A@@@@@@@@@A@@@@@@@ADB@@B@@@B@DCHC@@@AB@@A@@@@BC@@B@B@B@@@BC@A@@B@D@BABA@@@@BB@AB@@@BAA@@@C@BAB@@B@@BA@@BA@@B@@@@B@ABBB@@BB@@@@D@@B@@@BB@ABD@@@ABB@BB@D@B@@A@@FAB@JB@@B@@@B@BAB@@@@A@ABAB@@C@A@@@A@AAA@A@@@A@A@@@@AA@@A@CA@@@@BA@A@@AA@@@@AA@@CCA@B@@ABA@A@AF@AC@@@A@@BC@@@A@@A@@@A@A@@@AA@@AA@@@AA@@BADA@@B@@@@A@@@@@A@@@@@AA@@@A@@@A@@@AACCA@A@@AA@@BA@@@@@A@A@A@@@@@A@@@A@A@A@@@A@A@@@@B@@A@@@@@AB@@@@@BCA@@AA@CA@A@A@@@A@@@@@AB@B@@@BAB@D@@@@@@A@@@A@A@A@@@@B@@@B@@@B@B@B@B@B@BAB@BABAB@@A@AB@BA@B@@@@@BB@@@@@@@@A@@@@@@@A@@@A@@@@@@@@B@@@@@@@@@AA@@@@@A@BB@BB@@B@@A@@@A@@@A@@B@@@@@B@@B@@B@@@@@@@AC@@B@@@@@BAA@@@BA@@@A@A@@@@@A@@@@B@@@B@D@@@@@AA@@@@@ABBB@@B@@@BBB@@BBA@B@@BB@@@@@@@@@@BBB@@@B@@B@@ADA@A@@@@A@AA@@@@B@BA@BB@BB@@B@@@@@@@@AB@@@@@B@@@B@@ABB@@@@BB@@A@@B@@@@B@@@B@@@B@@@@B@@@@@B@@A@@@@@BB@@@@BB@@BBB@@BB@DBBBB@@@BB@@BB@@BBD@B@@BF@BADCD@BA@@BBB@@A@@B@BA@@B@@@@@@@AA@@@@A@@@@AB@@@@BB@BBB@@@@A@A@ABA@@BAB@@@AAAA@@BC@@BAD@@AD@@@@@B@@@B@D@DAB@B@@@B@B@D@@@B@@@BB@B@BB@B@B@D@F@B@@B@@BBBBB@B@@@@B@@@B@@@@@B@@DBBB@@B@@BB@@@BA@@B@B@@AB@@@@@@@BBB@BBBBB@F@B@B@@@B@@@B@@@B@BA@@@C@@@@DA@@@ADA@@B@BB@@@@ABA@A@@@@@BB@BB@A@@BB@B@@@@@@@@AB@@A@@@@B@B@BAB@@@@@AB@B@B@B@B@@B@@@@@B@@@B@B@@@B@B@B@@@@@BAB@@@B@@BB@@@@@B@BABBB@@@B@@@@B@@@B@@B@B@@@@B@B@@@BBAB@@@B@@@@B@BB@@@BABA@@@@AAAA@A@@@AB@@A@@B@B@@BB@BA@@B@@@B@B@@B@@B@@A@@B@B@@B@AB@BB@@@@BA@@@@B@BABAB@@@@A@AB@@@BB@@@@BB@@@@BB@@B@@@B@BB@@B@@@B@B@@@BB@@@A@@B@A@AA@A@A@@@@@@@@@@DB@@@@B@@@@A@C@A@@D@@@D@B@@@@@BB@@@@B@@@@@@@@AAAHE`S@AOOAAQSGIIIEEEECCAAA@A@A@ACCECEKKECQMIICAEEIEEAAAAAOIEAYIIAEAUA]GGAE@OCIAKCKAKAGAE@KEUISGECCA@AA@K@QAI@K@OBE@U@Y@iB@@@BS@@BAB@B@BAB@@@@@B@B@B@@CBA@CBABA@GBC@CBCB@@@@@@@@EDED@@@@A@A@B@@CA@@@@@A@@B@@E@@@CB@@A@A@@@AB@@@A@A@@B@@@@A@@@AA@@@AA@BA@A@@A@@A@@AAB@@AA@@@@A@@@A@@BAB@A@@C@AA@@A@@@@@A@@@A@@@A@@@AA@@AA@@AAAAB@AA@@@@@A@@ABAB@@@B@B@BAB@BA@BB@@@B@BA@@B@AA@AB@@@@@@ABAA@@@@@@@@@AABB@ABB@A@@BA@A@A@A@A@@BA@AB@@ABA@@B@@A@@@AAA@A@@BA@A@A@A@A@@@A@@@ABA@@@AA@@@A@ABA@A@A@@@@@@A@@AA@@AA@@@@A@@@AA@@AAA@@@@CAA@@@@@@AA@@@@A@@@@A@@@@A@@@AAA@@@AAAA@@AA@@A@@@A@@AA@@@AA@@@@AA@A@@AAA@@A@A@A@@A@@AAA@A@A@@@@@@AAA@@@@AAB@@@@@BB@@@A@@BA@@@@@@@@@@@@@AA@AA@@@A@@AA@@A@@@@AAB@@A@@@@@A@@@@@A@@@@@AAA@A@AB@@AA@@A@A@@B@@A@@@ABA@@@@B@@A@BBB@@BA@@BB@@B@@@@@@@B@@@BA@@@CA@@B@@A@@@@@AC@AA@B@@@B@@@@@BA@AB@@A@@@@@@@A@A@@BAAAB@@ABCAA@A@A@ABA@@BA@AD@@B@@B@@@@@@A@ABA@@@AA@@AA@A@@@A@A@A@C@@@A@@@@CA@@@@@@CA@@AA@@A@@@AA@@@@AAA@AAA@A@AA@@@AAA@@A@@A@@@A@@@AA@@@A@@@A@@A@@A@A@A@ABC@@A@@@@@@@A@@A@@@@@@@@@@@@B@@A@@A@B@A@@AA@AAA@@@A@@AB@@C@@@A@@@A@ABA@ABA@@@ABAB@@ABC@@@A@@@@@AA@@AAAAA@@@E@A@@@AB@BAAA@@@A@AB@B@@A@@@A@@@@B@@AB@@@@@A@@@EB@@@@ABAB@@@@A@@B@@@@@@@AA@@B@@@@AA@B@@@BA@@B@@B@A@@@@@A@@@A@@@@AA@@@@ABEDA@@A@@BAA@@@A@@@@AAC@@@@A@@@@BA@CAAA@@BA@@@A@@A@@@ABAB@@@@A@@A@@@@BA@AB@@@@@B@@A@@B@@A@A@@B@BAB@@@B@@@@@B@@@@AAA@@@@@A@AB@@A@@B@@ABA@@BA@@B@BA@A@@AA@@A@AA@@AA@AA@AAA@@A@@@A@A@@@A@@@@@A@@A@A@A@@@A@@AA@@@A@@A@@AA@@AA@@@@@AAA@C@@@C@@@@AA@@@AAA@ACA@A@A@@@@@AA@@CAA@@@@A@@AAA@@@A@@@A@@@@C@@@AA@@A@"],"encodeOffsets":[[124157,30120]]}}],"UTF8Encoding":true});}));