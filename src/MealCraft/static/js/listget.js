

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
    document.getElementById("productDG").innerHTML = food["generic_name_fr"];
    document.getElementById("productFirm").innerHTML = food["brands"];
    document.getElementById("productCategory").innerHTML = food["categories"];

    document.getElementById("productImg").src = food["image_url"];
    document.getElementById("productQuantity").innerHTML = food['packagings'][1]["quantity_per_unit"];

}

function ListGet() {
    document.querySelectorAll('.list-item').forEach(function (card) {
        searchQuery = card.id;

        var data = getFoodsByCode(searchQuery);
        card.innerHTML = data["product_name"];
     });
}