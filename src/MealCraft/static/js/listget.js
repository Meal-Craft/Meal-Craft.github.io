// function getFoodsByCode(liste) {
//     document.querySelectorAll('.list-item').forEach(function (card) {
//         searchQuery = card.id;

//         var apiURL =
//             "https://world.openfoodfacts.net/api/v2/product/" +
//             encodeURIComponent(searchQuery)

//         var xhr = new XMLHttpRequest();
//         xhr.open("GET", apiURL, false);
//         xhr.send();

//         if (xhr.status === 200) {
//             var data = JSON.parse(xhr.responseText);
//             if ("product" in data) {
//                 var product = data["product"];
//                 console.log(product);
//                 return product;
//             }
//         }
//     });
// }

function getFoodsByCode(searchQuery) {
    var apiURL =
        "https://world.openfoodfacts.net/api/v2/product/" +
        encodeURIComponent(searchQuery)

    var xhr = new XMLHttpRequest();
    xhr.open("GET", apiURL, false);
    xhr.send();

    if (xhr.status === 200) {
        var data = JSON.parse(xhr.responseText);
        if ("product" in data) {
            var product = data["product"];
            return product;
        }
    }
}


function getInformation(searchQuery) {
    var food = getFoodsByCode(searchQuery)

    document.getElementById("productName").innerHTML = food["product_name"];
    document.getElementById("productCB").innerHTML = food["code"];
    document.getElementById("productDG").innerHTML = food["brands"];

    document.getElementById("productImg").src = food["image_url"];

}