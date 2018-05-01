var fs = require('fs');
var file = "triples.json";

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";

var selectData = function (db, callback) {
    //连接到表  
    var collection = db.collection('distant_supervised');
    //查询数据
    var whereStr = {};
    collection.find(whereStr).toArray(function (err, result) {
        if (err) {
            console.log('Error:' + err);
            return;
        }
        callback(result);
    });
}

MongoClient.connect(url, function (err, db) {
    if (err) throw err;
    console.log("数据库已创建!");
    //查询数据
    var dbo = db.db("relation_extraction");
    selectData(dbo, function (result) {
        console.info(__dirname + '/' + file)
        // console.info(result)
        fs.writeFile(file, JSON.stringify(result), 'utf8', function () {
            // 保存完成后的回调函数
            console.log("保存完成");
        });
        db.close();
    });
    console.log("数据库已关闭!");
});