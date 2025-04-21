class MexerFormInput extends HTMLElement {
    #template = document.getElementById('mexer-form-input-template').content;

    constructor() {
        super();
        const clone = this.#template.cloneNode(true);

        // if didn't find the element in question, don't care
        try {
            const labelElement = this.querySelector("label");
            const newLabel = clone.querySelector("label");
            labelElement.className = newLabel.className; // get class names from template
        } catch {}

        try {
            const newInput = clone.querySelector("input");
            const inputElement = this.querySelector("input");
            inputElement.className = newInput.className;
        } catch {}

        try {
            const newSelect = clone.querySelector("select");
            const selectElement = this.querySelector("select");
            selectElement.className = newSelect.className;
        } catch {}
    }
}

customElements.define('mexer-form-input', MexerFormInput);
