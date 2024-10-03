import { ApiService } from "@/services/api/api.service";

export class CrudService extends ApiService {
    constructor(resource) {
        super();
        this.resource = resource;
    }

    get(entity) {
        return this.$get(`${this.resource}${entity}`);
    }

    post(entity) {
        return this.$post(this.resource, entity);
    }

    put(entity) {
        return this.$put(`${this.resource}${entity.id}/`, entity);
    }

    delete(entity) {
        return this.$delete(`${this.resource}${entity.id}`);
    }
}