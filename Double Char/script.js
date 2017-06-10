function doubleChar(str) {
    // Your code here
    var arr = [];
    for (var i = 0; i<str.length;i++){
        arr.push(str[i]);
        arr.push(str[i]);
    }
console.log(arr);
    var rez = arr.join('');
    console.log(rez);
}
doubleChar("String");
