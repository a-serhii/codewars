function compareNumeric(a, b) {
    if (a > b) return 1;
    if (a < b) return -1;
}
var min = function(list){

    return list.sort(compareNumeric)[list.length-1];
}

var max = function(list){

    return list.sort(compareNumeric)[0];
}
console.log(min([-52, 56, 30, 29, -54, 0, -110]);