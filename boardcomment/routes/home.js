var express = require('express');
var router = express.Router();

// Home
router.get('/', function(req, res){
  res.render('home/homehome');
});
router.get('/about', function(req, res){
  res.render('home/itsme');
});

module.exports = router;
