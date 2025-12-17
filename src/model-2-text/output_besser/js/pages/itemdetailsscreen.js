/**
 * ItemDetailsScreen Page
 * Generated from ItemDetailsScreen screen definition
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

    async init() {
        console.log('Initializing ItemDetailsScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
        if (['PaymentScreen','CheckoutScreen'].includes('ItemDetailsScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('ItemDetailsScreen' === 'ItemDetailsScreen' && !this.params.id) {
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
                    <label for="contact-seller-button">ContactSellerButton</label>
                    <input type="text" id="contact-seller-button" name="ContactSellerButton"
                        placeholder="Start a conversation"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ContactSellerButton">Contact Seller</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="contact-seller-button">
                <h3>ContactSellerButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="donation-badge">DonationBadge</label>
                    <input type="text" id="donation-badge" name="DonationBadge"
                        placeholder="Donation"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="DonationBadge">DonationBadge</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="donation-badge">
                <h3>DonationBadge</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-price-field">ItemPriceField</label>
                    <input type="text" id="item-price-field" name="ItemPriceField"
                        placeholder="Price of the item (for sale)."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemPriceField">ItemPriceField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-price-field">
                <h3>ItemPriceField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-publication-date-field">ItemPublicationDateField</label>
                    <input type="text" id="item-publication-date-field" name="ItemPublicationDateField"
                        placeholder="Date when the item was published."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemPublicationDateField">ItemPublicationDateField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-publication-date-field">
                <h3>ItemPublicationDateField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-description-field">ItemDescriptionField</label>
                    <input type="text" id="item-description-field" name="ItemDescriptionField"
                        placeholder="Detailed description of the item."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemDescriptionField">ItemDescriptionField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-description-field">
                <h3>ItemDescriptionField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
                    <label for="add-review-button">AddReviewButton</label>
                    <input type="text" id="add-review-button" name="AddReviewButton"
                        placeholder="Write a review"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="AddReviewButton">Add Review</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="add-review-button">
                <h3>AddReviewButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-status-field">ItemStatusField</label>
                    <input type="text" id="item-status-field" name="ItemStatusField"
                        placeholder="Current status of the item"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemStatusField">ItemStatusField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-status-field">
                <h3>ItemStatusField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('DataList' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-tags-list">ItemTagsList</label>
                    <input type="text" id="item-tags-list" name="ItemTagsList"
                        placeholder="Tags for this item"
                        class="form-control"/>
                </div>`;
        } else if ('DataList' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemTagsList">ItemTagsList</button>`;
        } else if ('DataList' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-tags-list">
                <h3>ItemTagsList</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-title-field">ItemTitleField</label>
                    <input type="text" id="item-title-field" name="ItemTitleField"
                        placeholder="Title of the item."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemTitleField">ItemTitleField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-title-field">
                <h3>ItemTitleField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-transaction-type-field">ItemTransactionTypeField</label>
                    <input type="text" id="item-transaction-type-field" name="ItemTransactionTypeField"
                        placeholder="Transaction type (Donation/Sale/Exchange)."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemTransactionTypeField">ItemTransactionTypeField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-transaction-type-field">
                <h3>ItemTransactionTypeField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
                    <label for="pay-now-button">PayNowButton</label>
                    <input type="text" id="pay-now-button" name="PayNowButton"
                        placeholder="Pay now"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="PayNowButton">Pay Now</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="pay-now-button">
                <h3>PayNowButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
                    <label for="start-order-button">StartOrderButton</label>
                    <input type="text" id="start-order-button" name="StartOrderButton"
                        placeholder="Create an order"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="StartOrderButton">Start Order</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="start-order-button">
                <h3>StartOrderButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
                    <label for="suggest-exchange-button">SuggestExchangeButton</label>
                    <input type="text" id="suggest-exchange-button" name="SuggestExchangeButton"
                        placeholder="Suggest an exchange"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="SuggestExchangeButton">Suggest Exchange</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="suggest-exchange-button">
                <h3>SuggestExchangeButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="variant-selector">VariantSelector</label>
                    <input type="text" id="variant-selector" name="VariantSelector"
                        placeholder="Choose variant"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="VariantSelector">VariantSelector</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="variant-selector">
                <h3>VariantSelector</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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

        if ('InputField' === 'InputField') {
            elementsHtml += `
                <div class="form-group">
                    <label for="item-community-field">ItemCommunityField</label>
                    <input type="text" id="item-community-field" name="ItemCommunityField"
                        placeholder="Community where the item is listed."
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemCommunityField">ItemCommunityField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="item-community-field">
                <h3>ItemCommunityField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemDetailsScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemDetailsScreen' === 'ItemDetailsScreen') {
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
            <div class="page page-item-details-screen">
                <div class="page-header">
                    <h1 class="page-title">ItemDetailsScreen</h1>
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