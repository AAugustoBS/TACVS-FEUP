/**
 * SubcommunitySelectorScreen Page
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class subcommunityselectorscreenPage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }

    isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
    }

    async fetchData() {
    }

    async render() {
        // ---------- AUTH GUARD ----------

        // ---------- ITEM DETAILS GUARD ----------

        await this.fetchData();

        return `
            <h1>SubcommunitySelectorScreen</h1>
        `;
    }

    init() {}
}