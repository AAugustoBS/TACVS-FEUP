/**
 * Router - Single Page Application Router
 * Handles client-side routing for appName
 */

import { paymentscreenPage } from './pages/paymentscreen.js';
import { blankscreenPage } from './pages/blankscreen.js';
import { ratingslistscreenPage } from './pages/ratingslistscreen.js';
import { itemlistscreenPage } from './pages/itemlistscreen.js';
import { subcommunityselectorscreenPage } from './pages/subcommunityselectorscreen.js';
import { itemdetailsscreenPage } from './pages/itemdetailsscreen.js';

export class Router {
    constructor() {
        this.routes = [];
        this.currentRoute = null;
        this.setupRoutes();
    }
    
    /**
     * Setup application routes
     */
    setupRoutes() {
        this.routes = [
            {
                path: '/paymentscreen',
                name: 'PaymentScreen',
                title: 'PaymentScreen',
                handler: paymentscreenPage,
                params: {},
                isMain: false
            },            {
                path: '/blankscreen',
                name: 'BlankScreen',
                title: 'BlankScreen',
                handler: blankscreenPage,
                params: {},
                isMain: false
            },            {
                path: '/ratingslistscreen',
                name: 'RatingsListScreen',
                title: 'RatingsListScreen',
                handler: ratingslistscreenPage,
                params: {},
                isMain: false
            },            {
                path: '/itemlistscreen',
                name: 'ItemListScreen',
                title: 'ItemListScreen',
                handler: itemlistscreenPage,
                params: {},
                isMain: true
            },            {
                path: '/subcommunityselectorscreen',
                name: 'SubcommunitySelectorScreen',
                title: 'SubcommunitySelectorScreen',
                handler: subcommunityselectorscreenPage,
                params: {},
                isMain: false
            },            {
                path: '/itemdetailsscreen',
                name: 'ItemDetailsScreen',
                title: 'ItemDetailsScreen',
                handler: itemdetailsscreenPage,
                params: {},
                isMain: false
            }        ];
    }
    
    /**
     * Initialize router
     */
    init() {
        // Listen for hash changes
        window.addEventListener('hashchange', () => this.handleRoute());
        
        // Handle initial route
        this.handleRoute();
    }
    
    /**
     * Handle route change
     */
    async handleRoute() {
        let hash = window.location.hash.substring(1);
        
        // If no hash, default to main screen (isMain) or first route
        if (!hash || hash === '/') {
            const mainRoute = this.routes.find(r => r.isMain);
            const fallbackRoute = this.routes[0];
            const target = mainRoute || fallbackRoute;
            if (target) {
                hash = target.path;
                window.location.hash = hash;
            }
        }
        
        const route = this.matchRoute(hash);
        
        if (route) {
            await this.loadRoute(route, hash);
        } else {
            this.show404();
        }
    }
    
    /**
     * Match URL to route
     */
    matchRoute(url) {
        for (const route of this.routes) {
            const params = this.extractParams(route.path, url);
            if (params !== null) {
                return { ...route, params };
            }
        }
        return null;
    }
    
    /**
     * Extract parameters from URL based on route pattern
     */
    extractParams(pattern, url) {
        const patternParts = pattern.split('/');
        const urlParts = url.split('/');
        
        if (patternParts.length !== urlParts.length) {
            return null;
        }
        
        const params = {};
        
        for (let i = 0; i < patternParts.length; i++) {
            if (patternParts[i].startsWith(':')) {
                const paramName = patternParts[i].substring(1);
                params[paramName] = urlParts[i];
            } else if (patternParts[i] !== urlParts[i]) {
                return null;
            }
        }
        
        return params;
    }
    
    /**
     * Load and render route
     */
    async loadRoute(route, url) {
        try {
            // Update page title
            document.title = 'appName - ' + route.title;
            
            // Get main content container
            const mainContent = document.getElementById('main-content');
            if (!mainContent) {
                console.error('Main content container not found');
                return;
            }
            
            // Show loading state
            mainContent.innerHTML = `
                <div class="loading">
                    <div class="spinner"></div>
                    <p>Loading...</p>
                </div>
            `;
            
            // Create page instance and render
            const pageInstance = new route.handler(route.params);
            const content = await pageInstance.render();
            
            // Update content with animation
            mainContent.classList.add('page-exit');
            
            setTimeout(() => {
                mainContent.innerHTML = content;
                mainContent.classList.remove('page-exit');
                mainContent.classList.add('page-enter');
                
                // Initialize page
                pageInstance.init();
                
                // Remove enter animation class
                setTimeout(() => {
                    mainContent.classList.remove('page-enter');
                }, 300);
            }, 150);
            
            this.currentRoute = route;
            
        } catch (error) {
            console.error('Error loading route:', error);
            this.showError('Failed to load page');
        }
    }
    
    /**
     * Navigate to a path
     */
    navigate(path) {
        window.location.hash = path;
    }
    
    /**
     * Go back
     */
    back() {
        window.history.back();
    }
    
    /**
     * Show 404 page
     */
    show404() {
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
            mainContent.innerHTML = `
                <div class="empty-state">
                    <div class="empty-state-icon">🔍</div>
                    <h2 class="empty-state-title">Page Not Found</h2>
                    <p class="empty-state-description">
                        The page you're looking for doesn't exist.
                    </p>
                    <button class="action-button action-button-primary" onclick="window.location.hash='/'">
                        Go Home
                    </button>
                </div>
            `;
        }
    }
    
    /**
     * Show error page
     */
    showError(message) {
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
            mainContent.innerHTML = `
                <div class="error">
                    <h3>Error</h3>
                    <p>${message}</p>
                    <button class="action-button action-button-primary" onclick="location.reload()">
                        Reload Page
                    </button>
                </div>
            `;
        }
    }
}