/**
 * BlankScreen Page
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class blankscreenPage {
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
            <h1>BlankScreen</h1>
        `;
    }

    init() {}
}