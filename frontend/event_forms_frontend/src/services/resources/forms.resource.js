import { CrudService } from "@/services/api/crud.service";

export class FormsResource extends CrudService {
    constructor() {
        super("forms/");
    }

    getForms(params = {}) {
        let url = "";
        if (Object.keys(params).length > 0) {
            const searchParams = new URLSearchParams(params);
            url = `?${searchParams.toString()}`;
        }
        return this.get(url);
    }

    createForm(form) {
        return this.post(form);
    }

    getFormById(formId) {
        return this.$get(`${this.resource}${formId}`);
    }

    updateForm(form) {
        return this.put(form);
    }
}