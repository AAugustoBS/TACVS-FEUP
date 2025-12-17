/**
 * ItemListScreen Page
 * Generated from ItemListScreen screen definition
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

    async init() {
        console.log('Initializing ItemListScreen page', this.params);

        // Setup buttons or inputs (optional: reuse existing ComponentRegistry)
        this.setupActionHandlers();
        this.setupChat();
    }

    async fetchData() {
        try {
            if ('ItemListScreen' === 'ItemListScreen') {
                this.data.items = await ItemApi.getAll();
            } else if ('ItemListScreen' === 'ItemDetailsScreen') {
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
        if (['PaymentScreen','CheckoutScreen'].includes('ItemListScreen') && !this.isLoggedIn()) {
            window.location.hash = '#/loginscreen';
            return '';
        }

        // ---------- ITEM DETAILS GUARD ----------
        if ('ItemListScreen' === 'ItemDetailsScreen' && !this.params.id) {
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
                    <label for="tag-filter-field">TagFilterField</label>
                    <input type="text" id="tag-filter-field" name="TagFilterField"
                        placeholder="Filter items by tag"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="TagFilterField">TagFilterField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="tag-filter-field">
                <h3>TagFilterField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="transaction-type-filter-field">TransactionTypeFilterField</label>
                    <input type="text" id="transaction-type-filter-field" name="TransactionTypeFilterField"
                        placeholder="Filter by transaction type"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="TransactionTypeFilterField">TransactionTypeFilterField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="transaction-type-filter-field">
                <h3>TransactionTypeFilterField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="view-item-details-button">ViewItemDetailsButton</label>
                    <input type="text" id="view-item-details-button" name="ViewItemDetailsButton"
                        placeholder="Open selected item details"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ViewItemDetailsButton">View Details</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="view-item-details-button">
                <h3>ViewItemDetailsButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="community-filter-field">CommunityFilterField</label>
                    <input type="text" id="community-filter-field" name="CommunityFilterField"
                        placeholder="Filter items by community"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="CommunityFilterField">CommunityFilterField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="community-filter-field">
                <h3>CommunityFilterField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="expiry-filter-field">ExpiryFilterField</label>
                    <input type="text" id="expiry-filter-field" name="ExpiryFilterField"
                        placeholder="Filter by expiry"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ExpiryFilterField">ExpiryFilterField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="expiry-filter-field">
                <h3>ExpiryFilterField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="items-list">ItemsList</label>
                    <input type="text" id="items-list" name="ItemsList"
                        placeholder="List of available items"
                        class="form-control"/>
                </div>`;
        } else if ('DataList' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ItemsList">ItemsList</button>`;
        } else if ('DataList' === 'DataList') {
            elementsHtml += `<div class="data-list" id="items-list">
                <h3>ItemsList</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="profile-button">ProfileButton</label>
                    <input type="text" id="profile-button" name="ProfileButton"
                        placeholder="Open user profile"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="ProfileButton">Profile</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="profile-button">
                <h3>ProfileButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="register-button">RegisterButton</label>
                    <input type="text" id="register-button" name="RegisterButton"
                        placeholder="Go to registration"
                        class="form-control"/>
                </div>`;
        } else if ('Button' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="RegisterButton">Sign up</button>`;
        } else if ('Button' === 'DataList') {
            elementsHtml += `<div class="data-list" id="register-button">
                <h3>RegisterButton</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="search-items-field">SearchItemsField</label>
                    <input type="text" id="search-items-field" name="SearchItemsField"
                        placeholder="Search items"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="SearchItemsField">SearchItemsField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="search-items-field">
                <h3>SearchItemsField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
                    <label for="status-filter-field">StatusFilterField</label>
                    <input type="text" id="status-filter-field" name="StatusFilterField"
                        placeholder="Filter items by status"
                        class="form-control"/>
                </div>`;
        } else if ('InputField' === 'Button') {
            elementsHtml += `<button class="btn btn-primary" data-action="StatusFilterField">StatusFilterField</button>`;
        } else if ('InputField' === 'DataList') {
            elementsHtml += `<div class="data-list" id="status-filter-field">
                <h3>StatusFilterField</h3>
                <div class="list-items">`;

            // Inject dynamic item data if it's the item list screen
            if ('ItemListScreen' === 'ItemListScreen') {
                elementsHtml += this.data.items.map(item => `
                    <div class="item-card">
                        <h3>${item.title}</h3>
                        <p>${item.price} €</p>
                        <a href="#/itemdetailsscreen?id=${item.id}">View details</a>
                    </div>
                `).join('');
            }

            // Inject dynamic item data if it's the item details screen
            if ('ItemListScreen' === 'ItemDetailsScreen') {
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
            <div class="page page-item-list-screen">
                <div class="page-header">
                    <h1 class="page-title">ItemListScreen</h1>
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