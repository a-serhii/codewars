var capitals = function (word) {
  var rez = []
  var regexp = /A-Z/;
  console.log (word.search(/[A-Z]/g));
  for (var i in word){
    if (word[i] === regexp){
      rez.push(i)
    }
  }
  return rez
};
capitals('GoIt');