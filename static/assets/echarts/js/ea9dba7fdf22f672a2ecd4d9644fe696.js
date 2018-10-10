(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('蓬安县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"511323","properties":{"name":"蓬安县","cp":[106.412136,31.029091],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@AACJQBGA@@@A@EBC@EBC@ABCBE@A@A@EBAAAAC@AAAA@AAA@AA@CBAAA@ABA@CBC@@@ABA@AB@BA@A@@@@AA@@A@A@EAACACAC@ABAACAA@A@@@ABAJCDAD@@CBEBABEBAB@BAF@B@@@B@@@B@B@B@B@B@BC@CBA@A@@@@BAB@B@D@B@D@D@B@D@BCHFHB@@B@B@@AB@@EBA@C@E@A@CBC@CBCBAAA@CHGF@B@@C@C@C@CBCBC@CBC@A@@BAD@BA@CBAACAC@C@EBADCDADCDCB@@EBCBCBIBA@EAA@ACACA@CAC@E@CBA@@BBFAFCJ@DABCBCBA@CAA@AA@@C@EBCBCBCBABAB@BAB@D@D@@@@BBAB@B@@@B@DABABCBABCD@DADBBCDABABCBE@C@ABA@CDA@BBEFCDADIHCDCBAD@DADE@A@IEC@EBGFCBC@CA@@C@@BA@ABA@C@A@A@AB@B@B@BA@A@AA@ABC@@@A@CBAA@A@A@AAA@A@AD@B@B@B@BEBIBA@A@@BAFABC@CBEBA@ABAB@BAD@BADBDBBB@JKNIHADABB@BBBBBBBBBDBDBFDDBHBFBB@B@B@B@D@B@BB@B@D@BABABABC@CBABCBABCBBB@BABCBEBA@C@@B@BBB@DABAB@B@BBD@D@DCBCBC@CBADAD@DBD@BBB@DBDADCDADCB@BABCBKFEFGDA@CBA@@DABAFEFSNCDCDABA@CAAAAAAM@AAAAAA@@B@B@BABA@A@AAABEHEBA@AADEAAAAC@@A@@A@@A@@A@@AB@@@ACAACBAB@@A@ABABADABA@EAECEAG@MDKBGDCBABBBB@B@FBDB@BAD@BBF@@BBB@@B@@@@@@@@@BABB@BBDBFBB@@B@@@B@BA@@BA@@@A@@@AB@D@@ABGB@BA@@B@BDB@@BB@@BF@BB@BABABA@ABAB@BBBBB@DBF@B@B@BABAB@BBBB@BBB@B@B@@ABCDCBA@CBA@C@A@@AC@AAC@C@A@CBAB@BAB@DABA@A@C@A@A@@@@B@B@B@D@@ADADCDCDCDADABA@CAEBE@A@AB@B@DB@@BBDBBBD@D@D@BAB@D@B@B@B@D@B@BBBDBB@D@DB@B@BCBEBADAB@BBBBHBBAB@@A@ECC@A@C@ABABBBBB@BB@@BA@@BBBDBFB@B@@@BABCBCBAB@BBBDADBB@BBBBBBBBBBDAFAB@B@FBDBB@B@@A@C@ABCBCB@D@BBBB@BDBDAD@FBDB@BDDDF@@@F@JBFDDFFFBD@F@B@DBB@B@B@@BA@ABA@@B@BD@BB@@@BA@@BAB@BAAA@AB@D@B@BDBD@B@B@FBDBB@DBB@BBD@DBB@FBBBJFADAD@H@DBFFH@B@DBBBD@D@DAF@D@B@@BBB@FDHDDD@D@DABCBABAB@@@B@BAB@@AB@B@BABA@AA@@AB@B@BAB@@@D@@B@D@B@B@@BBB@B@BB@DBD@D@BBBBB@B@BABA@AAA@AB@B@BBB@D@BABA@BB@@B@B@BBBB@BA@A@CBAD@D@DBDBD@B@B@@ABAAA@A@@@AACAC@@@A@CACACAC@AA@A@C@AA@@AAACAA@C@CDABBB@BDDB@@B@@@BABADAB@D@D@DDBBBB@D@F@D@FBDBDBBDDDBBBBF@BBB@BBDDDDBDBBBBBDBD@JDD@DBD@B@DB@B@DBHBFBFDDB@HBF@H@LAJ@FBDFBFBDBB@@BBBDDBDBDBB@DBFBDBDDBF@BBD@@BBD@D@D@FBDBB@DABEDA@CDEDABADADABCB@BADAD@D@DDBBBDBBBBF@D@F@BDBBDBB@HCDCDCFAD@B@FBB@BDDBF@B@B@H@D@B@@A@A@A@ABA@AB@B@B@BDB@BBD@H@D@DBBA@@@@@CA@@A@@AC@@@A@AB@@A@@B@@@D@@@@@B@@@D@D@B@@@@@B@@@BB@@BB@@@B@@@D@@@B@BDABA@A@@BA@ACA@A@EACAAAAGACA@AAA@CAGCGAC@A@C@C@AECC@AAC@AACA@@EAA@CAA@@AACCCCCAAAABABCDEBE@C@AACAAECQCA@AACCCCC@C@A@MDA@E@EAC@AA@A@A@CBA@CAEAAA@A@CBA@A@@@AAAA@C@GAC@G@C@C@C@AA@AAA@A@@A@A@C@C@E@ACACAAAA@@A@@BAHBB@BABC@C@C@ABAB@BAFBD@B@BABABCDCDEBCBAAACC@CAABCC@@A@ABAB@DBD@B@@ABC@AB@D@BA@@BA@AAABAB@DCDADCDAD@B@@@@B@BA@@BBBB@BAD@B@BA@C@A@A@G@@@@A@A@ABAA@@A@AAA@ABA@GAA@CAC@A@@@@AA@AAA@@@A@ABA@A@@AAAAG@C@A@@AAA@AA@A@E@C@@AACC@ADABADAHABBD@DBB@BA@A@AAA@A@C@G@ABCBCD@BA@C@ADAB@FAB@BCBA@A@K@C@@BABA@ABAAC@A@A@A@ABAFC@ADC@AB@B@H@FADABCDAB@B@D@F@B@BBDDF@D@D@FDDBB@D@D@DABEDADAFBPBJDJ@FAF@HBDBDA@ABCACCECE@A@CD@FDF@BAB@JCBCACBABABABA@A@@D@B@B@@@BA@ABA@C@ABC@A@@BAD@B@B@DAD@BABA@ABA@ABA@AA@@AAA@A@@AAAB@@ABA@@AAAAA@AA@ABC@A@AAC@ABA@ABA@@@AC@@@A@GA@@A@@A@E@AACA@A@ABCBCBC@E@ABAF@L@FAB@BCBA@@AAAAACAAAA@A@A@CBADABEHSDAFAF@DBBBBJDBFBBBBA@ABABCB@@ABAAA@A@A@@@AB@BAB@BABA@@B@@@@A@A@AA@DA@AB@DA@AD@DAD@BABBB@DJB@B@D@LA@@B@B@@BDFBBBB@BBBB@B@DABAD@H@D@B@B@DA@AAA@A@A@CBADADCFADEFCDADEBADCBCBCBE@A@CAC@@@ECCAAEAEACCAEAC@@@A@CB@DEBA@EAI@AAACCCA@A@A@C@@@A@@B@B@@@@A@@@EABCBC@A@A@@@@AAAB@@ABA@A@@@A@@AAA@CCA@AAA@ACA@A@EBE@IDCAC@CCECCC@AA@GCGA@@CDCFCBCBE@A@A@AA@ABCDA@A@A@A@CAC@AAEAA@A@A@C@A@@@A@CBCBABABABCBABABADABC@A@AACACAAACAE@CACAC@C@A@C@AAAKCOECAC@G@A@AAC@AAC@@@A@@@IAAAAA"],"encodeOffsets":[[109141,31494]]}}],"UTF8Encoding":true});}));