/**
 * PaymentScreen Page
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class paymentscreenPage {
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
 
        if (!this.isLoggedIn()) {
            if (window.location.hash.toLowerCase() !== '#/loginscreen') {
                window.location.hash = '#/loginscreen';
            }
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------

        await this.fetchData();

        return `
            <h1>PaymentScreen</h1>
        `;
    }

    init() {}
}