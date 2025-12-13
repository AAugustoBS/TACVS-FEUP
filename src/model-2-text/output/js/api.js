/**
 * API Service
 * Handles all API communication for Ballet Swap
 */

const API_BASE_URL = 'http://localhost:3000/api'; // Configure your backend URL

export class ApiService {
    /**
     * Generic fetch wrapper
     */
    static async fetch(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        
        const config = { ...defaultOptions, ...options };
        
        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }
    
    /**
     * GET request
     */
    static async get(endpoint) {
        return this.fetch(endpoint, { method: 'GET' });
    }
    
    /**
     * POST request
     */
    static async post(endpoint, data) {
        return this.fetch(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }
    
    /**
     * PUT request
     */
    static async put(endpoint, data) {
        return this.fetch(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    }
    
    /**
     * DELETE request
     */
    static async delete(endpoint) {
        return this.fetch(endpoint, { method: 'DELETE' });
    }
}

// Entity-specific API methods
export class ItemApi {
    static async getAll() {
        // Mock data for demonstration
        return [
            {
                id: 1,
                title: 'Ballet Shoes',
                price: 45.00,
                location: 'New York, NY',
                rating: 4.5,
                image: 'https://via.placeholder.com/300x200?text=Ballet+Shoes',
                category: 'Footwear',
                description: 'Professional ballet shoes in excellent condition.'
            },
            {
                id: 2,
                title: 'Tutu',
                price: 120.00,
                location: 'Los Angeles, CA',
                rating: 5.0,
                image: 'https://via.placeholder.com/300x200?text=Tutu',
                category: 'Costumes',
                description: 'Beautiful classical tutu, perfect for performances.'
            },
            {
                id: 3,
                title: 'Ballet Barre',
                price: 200.00,
                location: 'Chicago, IL',
                rating: 4.0,
                image: 'https://via.placeholder.com/300x200?text=Ballet+Barre',
                category: 'Equipment',
                description: 'Portable ballet barre for home practice.'
            }
        ];
        // Uncomment when backend is ready:
        // return ApiService.get('/items');
    }
    
    static async getById(id) {
        // Mock data for demonstration
        const items = await this.getAll();
        return items.find(item => item.id == id);
        // Uncomment when backend is ready:
        // return ApiService.get(`/items/${id}`);
    }
    
    static async create(data) {
        return ApiService.post('/items', data);
    }
    
    static async update(id, data) {
        return ApiService.put(`/items/${id}`, data);
    }
    
    static async delete(id) {
        return ApiService.delete(`/items/${id}`);
    }
}

export class ChatApi {
    static async getMessages(conversationId) {
        // Mock data for demonstration
        return [
            {
                id: 1,
                text: 'Hi! Is this item still available?',
                sent: false,
                timestamp: new Date(Date.now() - 3600000).toISOString()
            },
            {
                id: 2,
                text: 'Yes, it is! Would you like to know more?',
                sent: true,
                timestamp: new Date(Date.now() - 3000000).toISOString()
            },
            {
                id: 3,
                text: 'Can we meet tomorrow to see it?',
                sent: false,
                timestamp: new Date(Date.now() - 1800000).toISOString()
            }
        ];
        // Uncomment when backend is ready:
        // return ApiService.get(`/conversations/${conversationId}/messages`);
    }
    
    static async sendMessage(conversationId, text) {
        // Mock implementation
        return {
            id: Date.now(),
            text,
            sent: true,
            timestamp: new Date().toISOString()
        };
        // Uncomment when backend is ready:
        // return ApiService.post(`/conversations/${conversationId}/messages`, { text });
    }
}