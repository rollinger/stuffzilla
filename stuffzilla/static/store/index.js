import Vue from 'vue'
import Vuex from 'vuex'
// load vuex i18n module
import vuexI18n from 'vuex-i18n';

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {

    }
})

//vuexI18n Configuration https://github.com/dkfbasel/vuex-i18n
const config = {
	moduleName: 'i18n',
}
Vue.use(vuexI18n.plugin, store, config);

// define default translations for english text
import { localeEn } from '../locale/en/translationsEn.js'
import { localeDe } from '../locale/de/translationsDe.js'
import { localeEs } from '../locale/es/translationsEs.js'
import { localePt } from '../locale/pt/translationsPt.js'
// add the english locale to the i18n store
Vue.i18n.add('en', localeEn);
Vue.i18n.add('de', localeDe);
Vue.i18n.add('pt', localePt);
Vue.i18n.add('es', localeEs);
// set fallback language
Vue.i18n.fallback('en')
// set the current language to whatever gets interpolated in the <html lang> attribute
var lang = document.documentElement.getAttribute('lang') || 'en';
Vue.i18n.set(lang);
