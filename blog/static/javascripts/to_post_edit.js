function add_images(name, pk) {
    var select = document.getElementById('id_category');
    var option = document.cleateElement('option');
    option.setAttribute('value', pk);
    option.innerHTML = name;

    select.addEventListener(option, 0)
    select.options[0].selected = true
}