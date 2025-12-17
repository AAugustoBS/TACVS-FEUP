/**
 * PaymentScreen Page
 * Generated from PaymentScreen screen definition
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

    async init() {
        console.log('Initializing PaymentScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('PaymentScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('PaymentScreen' === 'ItemDetailsScreen') {
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
        if (['PaymentScreen','CheckoutScreen'].includes('PaymentScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('PaymentScreen' === 'ItemDetailsScreen' && !this.params.id) {
            window.location.hash = '#/itemlistscreen';
            return '';
        }

        await this.fetchData();

        if (this.data.error) {
            return `<div class="error"><h3>Error</h3><p>${this.data.error}</p></div>`;
        }

        // ---------- RENDER ORIGINAL UI ----------
        let elementsHtml = '';

        if ('Button' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="multibanco-button">MultibancoButton</label>
                    <input type="text" id="multibanco-button" name="MultibancoButton"
                        placeholder="Pay with Multibanco"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="MultibancoButton">Pay with Multibanco</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="multibanco-button">
                <h3>MultibancoButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('PaymentScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('PaymentScreen' === 'ItemDetailsScreen') {
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

        if ('Button' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="pay-pal-button">PayPalButton</label>
                    <input type="text" id="pay-pal-button" name="PayPalButton"
                        placeholder="Pay with PayPal"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="PayPalButton">Pay with PayPal</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="pay-pal-button">
                <h3>PayPalButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('PaymentScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('PaymentScreen' === 'ItemDetailsScreen') {
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

        if ('Button' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="mb-way-button">MBWayButton</label>
                    <input type="text" id="mb-way-button" name="MBWayButton"
                        placeholder="Pay with MBWay"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="MBWayButton">Pay with MBWay</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="mb-way-button">
                <h3>MBWayButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('PaymentScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('PaymentScreen' === 'ItemDetailsScreen') {
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
            <div class="page page-payment-screen">
                <div class="page-header">
                    <h1 class="page-title">PaymentScreen</h1>
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