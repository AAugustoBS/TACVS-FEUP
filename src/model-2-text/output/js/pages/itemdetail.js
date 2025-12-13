/**
 * Listing Page
 * Generated from ItemDetail screen definition
 */

import { ComponentRegistry } from '../components.js';
import { ItemApi } from '../api.js';

export class itemdetailPage {
    constructor(params = {}) {
        this.params = params;
        this.components = new ComponentRegistry();
        this.data = {};
    }
    
    /**
     * Initialize page after rendering
     */
    async init() {
        console.log('Initializing ItemDetail page', this.params);
        
        // Setup action button handlers
        this.setupActionHandlers();
        
    }
    
    /**
     * Fetch page data
     */
    async fetchData() {
        try {
            
            // Fetch item details
            if (this.params.id) {
                this.data.item = await ItemApi.getById(this.params.id);
            }
            
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
            <div class="page page-item-detail">
                <div class="page-header">
                    <h1 class="page-title">Listing</h1>
                </div>
                
                <div class="page-content">
                    ${this.components.render('DetailView', {
                        item: this.data.item,
                        entity: 'Item',
                        id: 'detail-main'
                    })}
                    ${this.components.render('ActionButton', {
                        label: 'Chat with seller',
                        icon: 'chat',
                        actionType: 'navigate' === 'navigate' ? 'primary' : 'secondary',
                        targetPath: '/chat/:conversationId',
                        id: 'detail-chat'
                    })}
                </div>
            </div>
        `;
    }
    
    /**
     * Setup action button handlers
     */
    setupActionHandlers() {
        const btn2 = document.getElementById('detail-chat');
        if (btn2) {
            btn2.addEventListener('click', () => {
                window.location.hash = '/chat/:conversationId';
            });
        }
    }
    
}