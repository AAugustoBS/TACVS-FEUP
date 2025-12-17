/**
 * ItemListScreen Page
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class itemlistscreenPage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }

    isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
    }

    async fetchData() {
        this.data.items = await ItemApi.getAll();
    }

    async render() {
        // ---------- AUTH GUARD ----------

        // ---------- ITEM DETAILS GUARD ----------

        await this.fetchData();

        return `
            <h1>Items</h1>
            <div class="list-items">
                ${this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">
                            View details
                        </a>
                    </div>
                `).join('')}
            </div>
        `;
    }

    init() {}
}