function getFoodsByCode(liste) {
    document.querySelectorAll('.list-item').forEach(function (card) {
        searchQuery = card.id;

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

                if ("product_name" in product) {
                    document.getElementById(searchQuery).innerText = product["product_name"];
                
                    return product["product_name"];
                }
            }
        }
    });
}
