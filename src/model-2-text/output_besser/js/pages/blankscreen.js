/**
 * BlankScreen Page
 * Generated from BlankScreen screen definition
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

    async init() {
        console.log('Initializing BlankScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('BlankScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('BlankScreen' === 'ItemDetailsScreen') {
                if (this.params.id) {
                    this.data.item = await ItemApi.getById(this.params.id);
                }
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            this.data.error = 'Failed to load data';
        }
    }

    async render() {
        // ---------- AUTH GUARD ----------
        if (['PaymentScreen','CheckoutScreen'].includes('BlankScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('BlankScreen' === 'ItemDetailsScreen' && !this.params.id) {
            window.location.hash = '#/itemlistscreen';
            return '';
        }

        await this.fetchData();

        if (this.data.error) {
            return `<div class="error"><h3>Error</h3><p>${this.data.error}</p></div>`;
        }

        // ---------- RENDER ORIGINAL UI ----------
        let elementsHtml = '';

        return `
            <div class="page page-blank-screen">
                <div class="page-header">
                    <h1 class="page-title">BlankScreen</h1>
                </div>
                <div class="page-content">
                    ${elementsHtml || '<div class="placeholder-content"><p>This screen has no UI elements defined in the model.</p></div>'}
                </div>
            </div>
        `;
    }

    setupActionHandlers() {
        // Setup your buttons, click handlers, or other component actions here
    }

    setupChat() {
        // Setup chat or conversation handlers here
    }
}