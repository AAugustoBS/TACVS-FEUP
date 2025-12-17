export class itemdetailsscreenPage {

    constructor(params = {}) {
        this.params = params;
    }

    async render() {

        if (!this.params.id) {
            return `
                <p>No item selected.</p>
                <a href="#/itemlistscreen">Back</a>
            `;
        }

        return `
            <h1>Item Details</h1>
            <p>Item ID: ${this.params.id}</p>
            <a href="#/itemlistscreen">Back to list</a>
        `;
    }

    init() {
        // Optional: attach events later
    }
}