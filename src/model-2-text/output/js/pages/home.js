/**
 * Ballet Swap Page
 * Generated from Home screen definition
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class homePage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }
    
    /**
     * Initialize page after rendering
     */
    async init() {
        console.log('Initializing Home page', this.params);
        
        // Setup action button handlers
        this.setupActionHandlers();
        
    }
    
    /**
     * Fetch page data
     */
    async fetchData() {
        try {
            // Fetch list items
            this.data.items = await ItemApi.getAll();
            
            
        } catch (error) {
            console.error('Error fetching data:', error);
            this.data.error = 'Failed to load data';
        }
    }
    
    /**
     * Render page content
     */
    async render() {
        // Fetch data before rendering
        await this.fetchData();
        
        if (this.data.error) {
            return `
                <div class="error">
                    <h3>Error</h3>
                    <p>${this.data.error}</p>
                </div>
            `;
        }
        
        return `
            <div class="page page-home">
                <div class="page-header">
                    <h1 class="page-title">Ballet Swap</h1>
                </div>
                
                <div class="page-content">
                    ${this.components.render('ListView', {
                        items: this.data.items || [],
                        entity: 'Item',
                        showImage: true,
                        showPrice: true,
                        showLocation: true,
                        showRating: true,
                        id: 'home-list'
                    })}
                    ${this.components.render('ActionButton', {
                        label: 'New Listing',
                        icon: 'plus',
                        actionType: 'navigate' === 'navigate' ? 'primary' : 'secondary',
                        targetPath: '/items/new',
                        id: 'home-new-item'
                    })}
                </div>
            </div>
        `;
    }
    
    /**
     * Setup action button handlers
     */
    setupActionHandlers() {
        const btn2 = document.getElementById('home-new-item');
        if (btn2) {
            btn2.addEventListener('click', () => {
                window.location.hash = '/items/new';
            });
        }
    }
    
}