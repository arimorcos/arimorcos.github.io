function showHideBibtex(curr_paper) {
    let bibtex_element = document.querySelector(curr_paper.concat("> span > div.bibtex"))
    if (bibtex_element.style.display === "") {
        bibtex_element.style.display = "block"
    } else {
        bibtex_element.style.display = ""
    }
}

function copyBibtex(curr_paper) {
    let bibtex_element = document.querySelector(curr_paper.concat("> span > div.bibtex"))

    // Make text area
    const text_area = document.createElement('textarea');
    text_area.value = bibtex_element.innerText;
    text_area.setAttribute('readonly', '');
    text_area.style.position = 'absolute';
    text_area.style.left = '-9999px';
    document.body.appendChild(text_area);

    // Select
    text_area.select();
    text_area.setSelectionRange(0, 99999)

    // Copy
    document.execCommand("copy");

    // Delete
    document.body.removeChild(text_area);

}

