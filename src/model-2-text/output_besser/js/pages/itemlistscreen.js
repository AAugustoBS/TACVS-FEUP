export class itemlistscreenPage {

    constructor(params = {}) {
        this.params = params;
    }

    async render() {

        return `
            <h1>Items</h1>
            <ul>
                <li><a href="#/itemdetailsscreen?id=1">Item 1</a></li>
                <li><a href="#/itemdetailsscreen?id=2">Item 2</a></li>
                <li><a href="#/itemdetailsscreen?id=3">Item 3</a></li>
            </ul>
        `;
    }

    init() {
        // Optional: attach events later
    }
}