(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('阿鲁科尔沁旗', {"type":"FeatureCollection","features":[{"type":"Feature","id":"150421","properties":{"name":"阿鲁科尔沁旗","cp":[120.0657,43.872298],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@ICOIK@IGQACBWBHNGLAJD@ADEAEPAFKDEAWFaVGFWPKHQLzvAhRhP@HV[NDFKJMJWTUFSF]N@@[EFCLGHMPA^DtC@EFCFEAkGQC@¥QYDqHsJPEFMDMJABB@BBIFMLMJABOJ@@NAJDJBLB`EFD@JAJLHDD@FFFEHBDA`JDEFI@AN_ND^EFEFKNDBX@H@B@@A@AB@NR@B@@@BA@@BABBBB@@B@@AD@@BBHBBBB@LJFH@BFF@BBB@B@@VNHFB@BBLFB@B@D@NFJBXFHBLBFJEHABCRBF@@DD\\RKNGDGDPFLBAFPBC^MAMPC@UEGHS@_ZW^EXDDARCBILFH@DADDHCFHD@@AJFB@DBFEBBDABO@CDABEHAD@BEBGDGDIDGFCFGD@@°EBBFLTCJAJCB@B@@G@@BAFC@CBC@E@CBE@E@@@C@ABAB@BEF@B@@BDD@BBD@DBBBDDAB@B@BEDC@ABABADCBADEFCFED@FBB@DFJFBDBDDEDABCBB@DFDLFDFFDF@@CD@F@HEHPFDPGDBNCHAHCFBPAB@B@@@@CBA@C@C@@@AB@BEB@@@BABABCBE@CBADA@@@C@CBABA@AAAAAAA@@BEBABAD@@ADABBFA@ABA@ABA@@BCB@BA@@BB@@DBB@@@BBB@B@B@B@@BF@@ABBB@BA@A@AB@DA@AB@@@BABABI@ABAB@B@B@B@BA@BB@@@@BB@@@BADAD@BADABCBB@@B@DA@CB@BA@@BABABC@@B@BCB@B@@BBAF@B@B@BCB@@@@@B@F@F@BB@@DDB@@@@BBAD@H@B@DAB@BCB@@A@A@CBA@ADABEFABABABAB@DBD@BB@B@@B@BB@@B@BABABA@@@@BCBAB@@AD@@EB@@AB@@@DAFABC@@BA@CB@@@BAB@BCDEDAB@BB@DB@B@@AB@@AB@B@B@BDFA@AD@BAB@B@D@BABB@ABBBBDAFBBBBDD@@CB@@BD@BDB@B@BDB@BFF@BA@@HBB@BAFBBFH@@F@FBBBBBB@DBD@FDL@B@@DBB@FBBBBD@BFA@ABAFCBAAA@ABCBA@ABAB@@DD@BDB@BBBDD@B@BBBB@BBCD@BBBAFBBB@@DA@CDCFDBBBDBBA@AB@NAFBBBHDBDH@DBF@BBHAB@B@ILABCDCDADA@AD@FA@CB@DBBBBADC@CBCB@BEF@DGBEBCBABBHB@@BFBBB@BBBABA@ADED@DAD@B@@B@B@@B@DFBAD@BFD@@@FA@ABAHA@@DCBEH@DA@C@A@A@@BAFABA@ABBBBJA@AD@D@DABABC@@B@DAB@BAD@D@BDBAB@D@@GJCBABA@ABA@ABCAEBGBADADCBABC@ABCDCB@@CFADAB@FCB@DABA@ABCAC@EBABCDED@FBDAB@BBBFF@B@HBBADA@CB@BDDB@@BCBAB@B@B@B@B@B@@@B@H@DB@B@BBBBBBBABBBBDBB@@DA@@BBB@B@DA@@F@B@@@B@D@@CBA@C@CBC@A@@B@DAD@B@FABAB@BABEF@@ADABA@ABID@D@@MJ@BDF@B@FAB@DDFB@@DE@E@C@EAC@E@CACAA@A@ECC@I@C@C@GCAAC@gLABAF@B@DBDAD@B@DADBD@BA@A@C@AB@@AFABABABCBA@A@ADAF@BEBABCDA@CBGD@BABCDA@@DDB@BCFCFABABED@BBB@JA@AFAB@BABED@B@D@B@DAB@BBB@BCD@BBDADBBAB@DABBBCBABE@CAQESGaKiQEDONA@C@CC@@AAAAACA@CAAA@E@@@AA@CAC@GAAAC@A@AACCA@C@AACAAAA@AACBABA@CBG@ABAFCBKBABABCDA@@@EAA@@@C@@@@B@@@D@@CD@D@@AD@B@@CDABABABADA@E@E@A@AB@BA@EBC@A@AACAA@CAAAA@C@ABA@CBEB@BAB@@AAB@AA@@AAA@A@ACIBCBGBCBAB@@A@@F@BABAB@@AB@@ABCDABCF@@ADB@ABABC@CFA@@DAB@@ABABAB@@@B@@@BBDBB@@@BCB@@@B@B@@DD@B@DABBBAD@@ABEDCBC@@AAAA@A@@@ABA@@FA@@@C@@@A@A@A@AB@@@@ABABCB@@AAEAA@@@@@A@@BA@ABA@@@ABADEB@@A@@B@@ABABAB@BA@@BA@A@AAABA@G@AB@B@B@@ABC@AAA@@BA@@BABABIDABA@@@A@ABC@AB@@@BBDBB@BAB@@CBOH@BAB@BAB@BBDB@@BB@@BB@AB@B@BDBBB@B@D@LDB@@BB@B@BAB@B@DA@@BBDBB@B@BBBB@BB@@BB@B@B@B@D@B@@@@@BAB@@C@ABAB@@@B@BA@BB@B@BCBAD@@@BB@BB@@BB@B@D@@@BBBDDBBBBB@DD@@@@@A@@@@@@@A@@@AB@B@@@@@B@@@@@DC@AB@@@@AB@@@B@@A@AB@@@@@BA@@B@B@@@@AB@@@B@B@F@BA@@@@B@B@@@DCB@@A@ABA@A@@B@B@B@BAF@H@BB@@BAD@B@@@@@B@B@@@B@B@@@B@B@DB@@B@@@@@BBB@BB@@D@DB@@B@@@B@D@@BB@BB@@D@B@@A@@B@B@@A@BB@@@BAB@BAB@B@D@BAB@@@B@B@B@D@B@B@B@L@F@F@BAB@BADAB@FAFAJ@D@DAD@DAHCFADAD@DAD@D@D@D@D@ABBD@@@BD@BB@BB@@B@@@BADADAB@B@BBB@@BD@BBB@B@B@B@DB@@B@@@@@@EBABCBEBAB@DABAB@BABA@@@A@A@EAC@ABA@@B@@@BA@@BA@@@EBA@ABCFCD@@A@@AA@AACCA@A@C@CBAB@@ADCBADABCBAB@B@B@@AB@@A@E@A@@@@@B@BBBB@@@B@BBBBB@@@BABAB@@ABA@@@@BB@@BAB@@@B@D@B@@C@ABG@AAC@@@A@@@@BB@@BAB@BA@BBAB@BCBCDABABC@@BB@B@DBBBDB@BBB@BAB@BA@@B@@@B@BBDBBB@B@B@BB@B@B@BBBBBBBDBBBB@DAFCPGDAF@DAFCDCHA@@DAD@BABCD@BAB@B@DBDBFBHBDBD@@@@B@@ABAB@D@DA@@B@BB@DBB@@@@B@B@@DDBDB@BB@@B@@@@@AB@@AB@B@BA@@@A@ABA@CDABA@ADA@@@@@CAA@AAC@A@G@GBABGDEBAB@@BB@B@BF@@@DBB@FDFDD@BB@@FDB@B@D@FBGDEBEDA@C@C@CB@@C@C@A@@BA@@@CCAAABA@A@A@AAC@KA@@@B@@BD@@ABCBAB@BCF@BA@ABABAB@BEDABGFEDIFED@BAF@B@BA@@BDR@DDPHFDFTVLPB@DBDBBHBBABB@@BD@B@BBB@@BDBDB@B@B@@BBB@B@@@@BBB@BDDDB@@BD@B@@BBF@D@BBB@FD@@B@@@BA@A@ABADADABADCB@BAB@FAJADAHAB@BAB@B@FAFADAB@B@DAB@B@BAB@B@B@BA@@BAD@DCB@B@BBD@BABAB@B@CBD@JEJIDE@EAEBIAIFICGHA@KF@J@NER@H@FELAHERCFFAFFFPDFJFFJHHHHHCDAHHDAFEHCJ@PAD@HMLIPFDLD@@CHCJKFOJMBQJEAGBKDOL@F@A@B@@@@EBA@@BADBB@BBD@@BF@F@DBF@BBBBDBB@@B@BBB@D@B@BBBBBD@D@@BF@BAHCHAD@B@@B@B@B@BBDBB@BDB@@BB@ABCBMDJDTE@PJDĊe²S^{XMgnY@@BARMFEHAFKFGDCF@DAFAJEH@FEDCHANBHABCBCBELCFEHCFCFEDIHIDGBEFCDCDKDMDI@E@G@GHE@GDGFEHEFC@EJIJOHQFED@DG@AA@BAAAB@@A@@AA@AAAB@@A@AACCGBCD@BAAAD@FABEBABA@ADCBC@AB@BGAA@AB@@AB@@AFEB@DC@ADABAAABADBACDAAAFCCA@A@EBGD@BCD@BCJAAABA@EB@@A@AFGA@@AD@@AFC@AD@DD@CF@BAF@B@@CDABB@BB@B@@AB@B@@@B@D@@A@ADAB@BBD@F@AA@AB@@BDA@AD@A@D@@CJ@BAH@DA@CD@@ALAFBB@@AFAD@DCD@BAD@DA@AFABAD@B@D@@ABABDFA@AB@BABBBAAABAFBDC@CB@DABCAADAF@@CA@ACFG@AB@@AHEAAB@B@D@A@FA@A@@B@HABB@AD@BA@@@@B@J@@AD@@@FAFA@AHABCD@@@@AFAAAF@BABAB@BAD@AA@@D@B@@CB@@@HC@ADABABAB@@AD@B@B@BADB@CB@B@AA@AD@BAB@BCA@@AA@DADC@AFEACDABCFBFC@CB@@AF@BCBCBA@CFA@ABADC@@FBFCACFABABB@CD@B@BA@@FAHEHKFGFCH@@GFBHADEBA`SNIbY@EFAFEHGNEFID@AEDAB@LA@ED@DACGFCDEJQAI@IAECDAEF@BI@CHAJC@IBKHG@GNK\\O\\KTGVIPCHAL@HAJBD@@@@@D@EKEGEKUOAIGO@ADGJIFILDHBJDNEDMHCF@LIHAJ_A@@ADEDAXCL@DGBAF@BADADCF@@EBE@ABC@ADEFCFCJATCD@B@FBD@RI@CAE@CBCDABAF@DBB@DCDABC@CDCAE@C@@IC@AEEBABABCBAFAJ@HGDABAAEBC@AHCAAFEI@HEAAADICDEKA@@AA@AHDDCFB@ADADCBBBC@@CCBA@AC@@ADA@ALEE@AAABECHEQcHGpoIBCGE@AB@@GEC@@@AFC@EBABE@KBA@ADAAGFABA@@@IFCBKB@BAF@BEBAJ@DABADA@@BCJEBCDCFA@AA@@EAEKAHIVYNOrq`BLAL@^YH@NB@@LhJBE@AHMBCFIJQT@N@FAF@J@F@J@D@J@F@J@DBF@P@JBHAVY@EAUCmGDQJ{V]_@@Q_ASwMQYGKCe@MX_NQLMPQ\\c^eFERSFQDC@@HC@@@@@LO`UBBG@I@@MGIEBikLGLKTUTSPMN_XMRKTQGEb[PE\\IXiXgXFAOUAAARE@@CCEIKGMBII@AKEDKCA@A@@CCABGGKCgG_MM@GAE@ECICSCKM@AMCEAE@IACEQGKEOIECEEEEQA_GGCIESEMEAE@GAIEKKICCCCECECUEAAEAIIAEGEEAMEA@OIYWAIIIKKOGOMQCOG]KEA_QIC]@i@aOSKYKIAQCgCUAcAGEQGMEUEICGGCE@AKAWAKCMCYAA@WFYCIBKAKAIDIFUHYHIHEBGBEBQEI@a@[@OCWAIAE@OBKAWASCUCMA_HMAKAOAA@"],"encodeOffsets":[[123013,44421]]}}],"UTF8Encoding":true});}));