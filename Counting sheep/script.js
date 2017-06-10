function countSheeps(arrayOfSheep) {
    var result = 0;
    for(i = 0; i < arrayOfSheep.length; i++) {
        if (arrayOfSheep[i]) {
            result++;
        }
    }
    return result;
}
var array1 = [true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ];

console.log(countSheeps(array1))




// function countSheeps(arrayOfSheep) {
//     var result = 0;
//     for (var key of arrayOfSheep){
//         if (key == true){
//             result+=1;
//         }
//     }
//     return result
// }
//
// var array1 = [true,  true,  true,  false,
//     true,  true,  true,  true ,
//     true,  false, true,  false,
//     true,  false, false, true ,
//     true,  true,  true,  true ,
//     false, false, true,  true ];
//
// alert(countSheeps(array1))