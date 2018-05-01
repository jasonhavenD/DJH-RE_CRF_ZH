var fs = require('fs');
var file = "triples.json";

var express = require('express');
var app = express();

var result = JSON.parse(fs.readFileSync(file));

// console.log(result)
var triples = [];
var entities = [];
var set = new Set();

// console.info(result[0]['e1'].trim());

for (var x of result) {
    e1 = x['e1'].trim();
    e2 = x['e2'].trim();
    triples.push(JSON.stringify(x));
    set.add(e1);
    set.add(e2);
}
for (var x of set) {
    entities.push(x);
}

// entities = ['小明', '小红', '小红红', '大明明', '大红红']
// var tpl1 = { 'e1': '小明', 'rel': 'like1', 'e2': '小红' }
// var tpl2 = { 'e1': '小明', 'rel': 'like2', 'e2': '小红红' }
// var tpl3 = { 'e1': '大明明', 'rel': 'like4', 'e2': '大红红' }
// triples = [JSON.stringify(tpl1),JSON.stringify(tpl2), JSON.stringify(tpl3)]

triples = triples.join('|')

var data = {
    entities: entities,
    triples: triples
};

app.set('view engine', 'ejs');

app.get('/index', function (req, res) {
    res.render('index', data)
})


var server = app.listen(8081, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("server has been started as : http://%s:%s", host, port)

})