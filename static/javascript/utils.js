function showHideBibtex(curr_paper) {
    let bibtex_element = document.querySelector(curr_paper.concat("> span > div.bibtex"))
    if (bibtex_element.style.display === "") {
        bibtex_element.style.display = "block"
    } else {
        bibtex_element.style.display = ""
    }
}