class MexerFormInput extends HTMLElement {
    #template = document.getElementById('mexer-form-input-template').content;

    constructor() {
        super();
        const clone = this.#template.cloneNode(true);

        try {
            const labelElement = this.querySelector("label");
            const newLabel = clone.querySelector("label");
            labelElement.className = newLabel.className; // get class names from template
        } catch {}

        const newInput = clone.querySelector("input");
        try {
            const inputElement = this.querySelector("input");
            inputElement.className = newInput.className;
        } catch {}

        try {
            const selectElement = this.querySelector("select");
            selectElement.className = newInput.className;
        } catch {}
    }
}

customElements.define('mexer-form-input', MexerFormInput);
