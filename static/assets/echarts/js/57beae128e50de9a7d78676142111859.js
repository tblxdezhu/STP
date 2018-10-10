(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('石家庄市长安区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"130102","properties":{"name":"长安区","cp":[114.539395,38.036347],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@G@@@C@C@@@@@G@G@@@A@A@@@A@@DEA@CC@@B@B@BA@@@@@@BE@@AC@@E@@@@@@I@@@E@@@@@A@@@@@@@@@A@@@@@I@@@A@@@@@@@I@@F@D@B@@@B@@A@@@@@A@@@@@@@@@A@@@A@@@@BA@@AB@A@@@@@@@@@@@@@@@A@@@@@@@@@@@@@A@@@@@@@A@@@@@@@@@A@@@@@@@@@@@A@@BA@@@E@A@@@G@A@@@BLBJ@@@@@D@@BHBJBJ@@BF@@BDBH@@BBBDA@QBBB@@@@BR@B@@@B@D@@@@@B@J@@BFGCAAA@OBCF@@@BB@H@@@BF@D@@@@DBBB@@I@HFBBFFBB@@FFJH@@BBDDB@F@D@D@D@F@B@D@DB@@DA@@F@B@FAHAFADABAD@FCFAFALAJAB@HELAHAD@D@F@LBB@B@DADCB@BAHCH@LABALBH@D@J@@@D@B@D@D@NCDAJAHCD@FAN@TGPDZB@C@ET@@ED@@@@EB@B@@@AKAG@EKQGMABCBC@A@CE@A@AG@@CA@ABEI@E@@@C@C@AA@C@@G@@BAkHA@EBQDKBKBEBKBYFC@aH@A@C@W@C@KG@K@C@E@@@A@I@C@E@G@@@"],"encodeOffsets":[[117312,38950]]}}],"UTF8Encoding":true});}));