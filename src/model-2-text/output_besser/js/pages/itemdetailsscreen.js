/**
 * ItemDetailsScreen Page
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class itemdetailsscreenPage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }

    isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
    }

    async fetchData() {
        if (!this.params.id) return;
        this.data.item = await ItemApi.getById(this.params.id);
    }

    async render() {
        // ---------- AUTH GUARD ----------

        // ---------- ITEM DETAILS GUARD ----------
        if (!this.params.id) {
            if (window.location.hash.toLowerCase() !== '#/itemlistscreen') {
                window.location.hash = '#/itemlistscreen';
            }
            return '';
        }

        await this.fetchData();

        if (!this.data.item) {
            if (window.location.hash.toLowerCase() !== '#/itemlistscreen') {
                window.location.hash = '#/itemlistscreen';
            }
            return '';
        }

        return `
            <h1>${this.data.item.title}</h1>
            <p>${this.data.item.description}</p>
            <p>Price: ${this.data.item.price} €</p>
            <a href="#/itemlistscreen">Back to list</a>
        `;
    }

    init() {}
}