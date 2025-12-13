/**
 * Component Registry and Renderers
 * Provides rendering functions for GUI components
 */

export class ComponentRegistry {
    constructor() {
        this.components = new Map();
        this.registerDefaultComponents();
    }
    
    /**
     * Register default component renderers
     */
    registerDefaultComponents() {
        this.register('ListView', ListViewComponent);
        this.register('DetailView', DetailViewComponent);
        this.register('ActionButton', ActionButtonComponent);
        this.register('ChatComponent', ChatComponent);
    }
    
    /**
     * Register a component renderer
     */
    register(type, component) {
        this.components.set(type, component);
    }
    
    /**
     * Get component renderer
     */
    get(type) {
        return this.components.get(type);
    }
    
    /**
     * Render a component
     */
    render(type, props = {}) {
        const Component = this.get(type);
        if (Component) {
            return new Component(props).render();
        }
        console.warn(`Component type "${type}" not found`);
        return '';
    }
}

/**
 * Base Component Class
 */
class Component {
    constructor(props = {}) {
        this.props = props;
    }
    
    render() {
        return '';
    }
}

/**
 * ListView Component
 */
class ListViewComponent extends Component {
    render() {
        const { items = [], entity = 'Item', showImage, showPrice, showLocation, showRating, id = 'list-view' } = this.props;
        
        if (items.length === 0) {
            return `
                <div class="component-listview" id="${id}">
                    <div class="empty-state">
                        <div class="empty-state-icon">📋</div>
                        <h3 class="empty-state-title">No ${entity}s Yet</h3>
                        <p class="empty-state-description">Start adding items to see them here.</p>
                    </div>
                </div>
            `;
        }
        
        const itemsHtml = items.map(item => `
            <div class="list-item" data-id="${item.id}" onclick="window.location.hash='/items/${item.id}'">
                ${showImage && item.image ? `
                    <img src="${item.image}" alt="${item.title || item.name}" class="list-item-image">
                ` : ''}
                <div class="list-item-content">
                    <h3 class="list-item-title">${item.title || item.name}</h3>
                    ${showPrice && item.price ? `<div class="list-item-price">$${item.price}</div>` : ''}
                    ${showLocation && item.location ? `<div class="list-item-location">📍 ${item.location}</div>` : ''}
                    ${showRating && item.rating ? `
                        <div class="list-item-rating">
                            <span class="rating-stars">${'⭐'.repeat(Math.floor(item.rating))}</span>
                            <span>(${item.rating})</span>
                        </div>
                    ` : ''}
                </div>
            </div>
        `).join('');
        
        return `
            <div class="component-listview" id="${id}">
                ${itemsHtml}
            </div>
        `;
    }
}

/**
 * DetailView Component
 */
class DetailViewComponent extends Component {
    render() {
        const { item, entity = 'Item', id = 'detail-view' } = this.props;
        
        if (!item) {
            return `
                <div class="component-detailview" id="${id}">
                    <div class="loading">
                        <div class="spinner"></div>
                        <p>Loading ${entity.toLowerCase()}...</p>
                    </div>
                </div>
            `;
        }
        
        return `
            <div class="component-detailview" id="${id}">
                ${item.image ? `<img src="${item.image}" alt="${item.title || item.name}" class="detail-image">` : ''}
                
                <h1 class="detail-title">${item.title || item.name}</h1>
                
                ${item.price ? `<div class="detail-price">$${item.price}</div>` : ''}
                
                <div class="detail-meta">
                    ${item.location ? `
                        <div class="detail-meta-item">
                            <span class="detail-meta-label">Location</span>
                            <span class="detail-meta-value">📍 ${item.location}</span>
                        </div>
                    ` : ''}
                    ${item.rating ? `
                        <div class="detail-meta-item">
                            <span class="detail-meta-label">Rating</span>
                            <span class="detail-meta-value">${'⭐'.repeat(Math.floor(item.rating))} (${item.rating})</span>
                        </div>
                    ` : ''}
                    ${item.category ? `
                        <div class="detail-meta-item">
                            <span class="detail-meta-label">Category</span>
                            <span class="detail-meta-value">${item.category}</span>
                        </div>
                    ` : ''}
                </div>
                
                ${item.description ? `
                    <div class="detail-section">
                        <h3 class="detail-section-title">Description</h3>
                        <div class="detail-section-content">${item.description}</div>
                    </div>
                ` : ''}
            </div>
        `;
    }
}

/**
 * ActionButton Component
 */
class ActionButtonComponent extends Component {
    render() {
        const { 
            label = 'Action', 
            icon = '', 
            actionType = 'primary',
            targetPath = '',
            id = 'action-btn',
            onClick = ''
        } = this.props;
        
        const iconHtml = icon ? `<span class="action-button-icon">${this.getIcon(icon)}</span>` : '';
        const clickHandler = onClick || (targetPath ? `window.location.hash='${targetPath}'` : '');
        
        return `
            <button 
                id="${id}" 
                class="action-button action-button-${actionType}"
                onclick="${clickHandler}"
            >
                ${iconHtml}
                <span>${label}</span>
            </button>
        `;
    }
    
    getIcon(iconName) {
        const icons = {
            'plus': '➕',
            'chat': '💬',
            'edit': '✏️',
            'delete': '🗑️',
            'save': '💾',
            'send': '📤',
            'back': '←',
            'forward': '→'
        };
        return icons[iconName] || iconName;
    }
}

/**
 * Chat Component
 */
class ChatComponent extends Component {
    render() {
        const { messages = [], conversationId = '', id = 'chat' } = this.props;
        
        const messagesHtml = messages.map(msg => `
            <div class="chat-message ${msg.sent ? 'sent' : 'received'}">
                <div class="chat-bubble">${msg.text}</div>
                <div class="chat-timestamp">${this.formatTimestamp(msg.timestamp)}</div>
            </div>
        `).join('');
        
        return `
            <div class="component-chatcomponent" id="${id}">
                <div class="chat-messages" id="chat-messages-${conversationId}">
                    ${messagesHtml || '<div class="empty-state"><p>No messages yet. Start the conversation!</p></div>'}
                </div>
                <div class="chat-input-container">
                    <input 
                        type="text" 
                        class="chat-input" 
                        id="chat-input-${conversationId}"
                        placeholder="Type a message..."
                        onkeypress="if(event.key==='Enter') this.nextElementSibling.click()"
                    >
                    <button class="chat-send-button" onclick="window.sendMessage('${conversationId}')">
                        Send
                    </button>
                </div>
            </div>
        `;
    }
    
    formatTimestamp(timestamp) {
        if (!timestamp) return '';
        const date = new Date(timestamp);
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
}

// Make ComponentRegistry available globally
if (typeof window !== 'undefined') {
    window.ComponentRegistry = ComponentRegistry;
}

export {
    Component,
    ListViewComponent,
    DetailViewComponent,
    ActionButtonComponent,
    ChatComponent
};