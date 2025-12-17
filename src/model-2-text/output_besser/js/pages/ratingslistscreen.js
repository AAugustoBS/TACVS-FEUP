/**
 * RatingsListScreen Page
 * Generated from RatingsListScreen screen definition
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class ratingslistscreenPage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }

    isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
    }

    async init() {
        console.log('Initializing RatingsListScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('RatingsListScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('RatingsListScreen' === 'ItemDetailsScreen') {
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
        if (['PaymentScreen','CheckoutScreen'].includes('RatingsListScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('RatingsListScreen' === 'ItemDetailsScreen' && !this.params.id) {
            window.location.hash = '#/itemlistscreen';
            return '';
        }

        await this.fetchData();

        if (this.data.error) {
            return `<div class="error"><h3>Error</h3><p>${this.data.error}</p></div>`;
        }

        // ---------- RENDER ORIGINAL UI ----------
        let elementsHtml = '';

        if ('DataList' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-reviews-list">ItemReviewsList</label>
                    <input type="text" id="item-reviews-list" name="ItemReviewsList"
                        placeholder="Reviews for this item"
                        class="form-control"/>
                </div>`;
        } else if ('DataList' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemReviewsList">ItemReviewsList</button>`;
        } else if ('DataList' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-reviews-list">
                <h3>ItemReviewsList</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('RatingsListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('RatingsListScreen' === 'ItemDetailsScreen') {
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
            <div class="page page-ratings-list-screen">
                <div class="page-header">
                    <h1 class="page-title">RatingsListScreen</h1>
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