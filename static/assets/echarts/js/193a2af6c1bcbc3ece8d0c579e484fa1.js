(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('井研县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"511124","properties":{"name":"井研县","cp":[104.069726,29.651287],"childNum":3},"geometry":{"type":"MultiPolygon","coordinates":[["@@@@@@@@@@@@@@@@"],["@@@@A@@@@@@@@B@@@@B@@A"],["@@AAAA@A@A@A@C@A@AAAEAAAA@EB@@A@@@@BABBB@@@BA@A@@@@@AA@A@@@@A@@@@@ABBB@@AF@@A@ABABA@E@CAA@@@A@A@CDA@A@@@A@AAA@AAECACCA@AAABAB@@A@AA@@A@@AAAC@AC@A@A@@@A@IAA@AAAAA@@@AB@B@@@@A@A@AAAA@BC@E@A@@A@A@CACAACAA@ABABD@BB@@@B@@AB@@C@C@AAA@A@AA@@BABABAB@BAB@@ABA@AA@@@ABAB@AACC@@A@I@AA@A@ABABAAE@A@A@@BAFA@BB@@BBADBF@B@@AD@@A@A@@BA@EJC@CDAB@@CBCA@@AAA@@AAA@AC@A@CBA@A@AB@@@BD@BB@@AB@@A@A@A@A@AB@B@BA@A@E@AAG@AAAA@ABAB@BA@@@@@AAEEC@AA@@@A@C@ABA@C@@@@@A@@@AAAA@AAAA@A@CAA@A@@B@@@B@BAB@@A@@AAA@B@@ADAB@F@@ADEDAB@B@B@BBDA@C@G@AAA@AEAAAAEBABE@CAEAC@C@AAAAA@CBAFAHABAA@@@ACAA@A@CFAD@B@DBD@BABA@EAGAC@A@CF@BC@ABAB@B@D@B@B@D@B@BBBB@B@F@JC@@F@F@BBBB@@@D@@AD@BAB@BBF@BB@B@B@FAB@BB@B@B@D@@FCD@B@B@@HBBBB@@B@@@@@@@BB@@@BEH@B@@@@@BB@@BB@DB@@@@B@@@B@@@@@B@@B@@BBBB@B@@BBDDFFBB@BDAB@DAB@BA@@@C@@AAA@CA@@D@D@B@B@BB@B@@@H@BADABAD@DB@F@DCDAB@D@B@BBBBBBAD@@EF@B@D@D@BBD@@NDB@@B@@@BABA@CFAB@B@B@@B@B@FBF@H@FBFBDBBB@BA@@BC@CBC@A@C@A@AF@@@@BBB@B@ABD@FBHD@B@@ABABA@@BAB@BA@ABA@CAA@CACAA@A@A@C@A@A@A@@BAB@@BB@BBFDJBBBBBBBBDBBBB@BBBAB@BADABCDCBABA@@BB@DBB@@BDBB@BAB@B@D@F@DBB@@DDHD@BHDFDDB@BBBABABA@CBCDC@ABC@ABABAFAB@B@@@B@BB@AB@D@@B@D@FAB@B@BB@@BB@B@BAB@@ABA@A@C@A@ABAB@B@B@D@F@B@@@BGB@B@BB@DBB@BB@@@DAD@B@DDJBJ@D@D@H@BBF@B@@EB@@@B@D@BABAACA@B@B@BB@@BBD@@BBFCB@BB@J@BAB@BBBDBD@LBBB@@FHBB@D@@@B@@ABABABAB@B@D@BA@AA@@CD@@A@@@@B@D@DADA@ABA@A@AA@@@ABA@AAA@@AAA@A@CBC@E@GBEDGFI@CBADBDBDDLBJBB@BBBB@BB@BAB@BABADABA@@D@@A@@AC@@A@AAAAA@AAAA@@AE@CA@@AAAAA@A@EBG@C@CBC@C@A@AAGCAAC@IBC@A@@@@AA@A@CCAAA@ABA@AB@BBD@B@B@F@H@DFPBBDBB@HED@BBBFAJABABKAABAD@BBFBBFA@BB@FDB@@@HDDBHBDB@BBH@DFFBBBBB@BBB@D@@BABGHABABCH@BBJ@F@BBBB@HBB@D@DBBBDB@@B@B@DABA@ABAB@BAB@BAHBB@LDBA@B@D@@@BADA@EBABABAFAB@BEB@D@BBBHBBBB@BBDDBH@BB@@@BABAB@@@DD@DDAB@DADAB@BCBAB@BAD@B@B@BBBB@BFBBBB@D@DBBB@BBBBB@@BBBBBB@BBDBBBDBBBBB@DBB@FAD@BADAB@FBB@D@DBBDFB@@DADABAB@@A@AB@B@B@@A@ADAFCB@B@DB@@@B@BBBB@BBB@B@@A@A@C@ABADADA@@BC@A@A@A@A@C@@@A@CAEAA@@AAAACECEA@CAC@@A@AAE@CBAB@D@@@BBBBB@BADABAB@D@B@B@D@FBFAB@B@FADABABA@A@C@C@C@@@CBCDAB@BBDBB@F@B@BA@@@A@A@A@C@A@EAAIAA@ACCCACAACE@AAA@CBA@AACAAAAC@A@G@AAAAAA@A@ABABAFC@@BABAHCBE@E@ABC@AB@BCB@DCBCBCB@D@BABABCBC@C@@BCBAB@DAB@HFB@B@JC@@F@BA@CAAACBADAB@@@B@@AB@B@B@D@DEDCBC@EBEBAB@DEBANCBABC@A@@BAD@FBD@B@DCDCB@B@DB@N@@BBB@FBF@D@DAH@D@DAB@BAB@B@B@B@DC@@BCBAB@@@DBD@B@BA@@B@@AB@@ABAA@@A@@AA@AAA@C@@CGAM@CBAH@FBDBBHBBB@BBB@B@BABA@AAACCACA@AA@A@C@ABAB@@A@AACBA@@BAB@B@BA@ABCAAAC@ABAB@B@B@BBB@B@F@B@FABB@@@B@FAD@BBBBAB@B@B@DDDBD@B@BADAB@BABC@A@AA@ACAA@A@A@A@CBC@@B@B@B@B@@A@@@A@@@@@@D@D@@A@A@AAACACA@@@ABCF@B@H@BAB@@C@@GAA@@A@A@A@@BADADAB@D@D@@@B@BAAACA@@E@E@CBC@A@@A@A@@BC@A@@BAB@B@DBDBBA@A@@@C@C@CBA@@DAB@@AAA@@MAA@@ABC@A@@AAABA@E@A@A@CAAAC@E@E@EBC@A@A@@AA@@CAAA@EBEB@@EDA@EB@@A@@BAB@J@BABA@KDA@AAA@@AABA@ABCJ@@ABA@A@A@@AC@AA@@@E@AAA@AAA@A@ABA@ABABC@A@@@AAA@@ACAACACAA@@AA@@AAAAE@@@G@AAA@@CAA@CBA@@AA@E@A@A@AACC@@AAA@A@@@CDA@ABAA@A@@@CAA@@C@@BABA@@@AA@@@CBABADCBADEBC@CBC@@BAHAFCHA@@BABC@@BA@CAA@A@A@A@@@ABAFAB@@A@A@A@A@A@A@A@C@@@ACEAA@@CEAAGAAAC@AAA@A@@A@AAAAA@A@@@@@AB@BA@AEE@@A@ABAB@@A@A@EA@@CAA@A@@AAA@E@C@AB@B@B@FBDBDBB@B@B@B@B@BAB@@ABCBABCBA@A@AAACAACCA@@AC@A@A@AB@B@B@BBBBBBBBB@BBD@D@B@@A@@EC@A@ABA@@@A@ABCD@BA@@@@BB@@BB@AB@@@@A@@A@@@@@@@AAB@@@@@@A@@@@@A@@CA@@AAAAEA@@@@@A@@B@D@B@@@@@@A@A@@AA@AAA@A@@@C@A@AAAAAAA@@AC@AA@AAAAA@C@C@@@A@@@@BAB@@@F@BABABCBABEB@DADABABABA@A@A@AAAA@@A@A@A@@B@B@BB@F@BB@@@B@@@BA@@@C@@@@@@@@D@@@B@@ABABA@A@A@AA@AAC@A@@CC@A@A@A@@AAA@@@AAA@E@A@@@AAA@@A@ACAAAEC@A@@@AA@EC@AAAAA@AA@@@A@A@@BA@@@"]],"encodeOffsets":[[[106667,30205]],[[106650,30178]],[[106595,30181]]]}}],"UTF8Encoding":true});}));