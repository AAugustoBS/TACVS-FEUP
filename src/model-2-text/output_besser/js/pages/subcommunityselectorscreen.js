/**
 * SubcommunitySelectorScreen Page
 * Generated from SubcommunitySelectorScreen screen definition
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

    async init() {
        console.log('Initializing SubcommunitySelectorScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('SubcommunitySelectorScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('SubcommunitySelectorScreen' === 'ItemDetailsScreen') {
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
        if (['PaymentScreen','CheckoutScreen'].includes('SubcommunitySelectorScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('SubcommunitySelectorScreen' === 'ItemDetailsScreen' && !this.params.id) {
            window.location.hash = '#/itemlistscreen';
            return '';
        }

        await this.fetchData();

        if (this.data.error) {
            return `<div class="error"><h3>Error</h3><p>${this.data.error}</p></div>`;
        }

        // ---------- RENDER ORIGINAL UI ----------
        let elementsHtml = '';

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="subcommunity-selector-field">SubcommunitySelectorField</label>
                    <input type="text" id="subcommunity-selector-field" name="SubcommunitySelectorField"
                        placeholder="Select subcommunity"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="SubcommunitySelectorField">SubcommunitySelectorField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="subcommunity-selector-field">
                <h3>SubcommunitySelectorField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('SubcommunitySelectorScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('SubcommunitySelectorScreen' === 'ItemDetailsScreen') {
                if (this.data.item) {
                    elementsHtml += `
                        <div class="item-card">
                            <h3>${this.data.item.title}</h3>
                            <p>${this.data.item.description}</p>
                            <p>Price: ${this.data.item.price} €</p>
                            <a href="#/itemlistscreen">Back to list</a>
                        </div>
                    `;
                } else {
                    elementsHtml += `<p class="placeholder-text">Item not found.</p>`;
                }
            }

            elementsHtml += `</div></div>`;
        }

        return `
            <div class="page page-subcommunity-selector-screen">
                <div class="page-header">
                    <h1 class="page-title">SubcommunitySelectorScreen</h1>
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