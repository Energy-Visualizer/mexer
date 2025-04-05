class MexerCard extends HTMLElement {
    #template = document.getElementById('mexer-card-template').content;

    constructor() {
        super();
        const clone = this.#template.cloneNode(true);

        const titleElement = this.querySelector("#title");
        clone.getElementById("title").innerHTML = titleElement.innerHTML;
        this.removeChild(titleElement);

        const contentElement = this.querySelector("#content");
        clone.getElementById("content").innerHTML = contentElement.innerHTML;
        this.removeChild(contentElement);

        this.appendChild(clone);
    }
}

customElements.define('mexer-card', MexerCard);
