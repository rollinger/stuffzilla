<!--
    Profile Component Documentation
    Structural component defining the main market view of Sharezilla
-->

<template lang="html">
    <!-- template code-->
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <div class="media mt-3">
                    <div class="media-body">

                        <div class="row">
                            <div class="col-sm-auto">
                                <img class="mr-3 mb-3" :src="profile.public_profile.user_image">
                            </div>

                            <div class="col-sm-8">
                                <h5 class="mt-0 mb-3">{{ $t( 'profile.your_profile' ) }}:</h5>
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.username' ) }}:</span>
                                    </div>
                                    <input type="text" readonly class="form-control form-control-plaintext" :value="profile.username">
                                </div>

                                <div class="input-group mt-1">
                                    <input type="file" class="form-control-file" :value="profile.public_profile.image">
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-sm-12">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.bio' ) }}:</span>
                                    </div>
                                    <textarea class="form-control" aria-label="$t( 'profile.bio' )" v-model="profile.public_profile.bio" v-on:change="updateUserProfile()"></textarea>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-sm-12">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.language' ) }}:</span>
                                    </div>
                                    <select class="form-control" aria-label="$t( 'profile.language' )" v-model="profile.private_profile.app_lang" v-on:change="updateUserProfile()">
                                        <option v-for="lang in languages" :value="lang.url">{{ lang.name }}</option>
                                    </select>
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.current_area' ) }}:</span>
                                    </div>
                                    <select class="form-control" aria-label="$t( 'profile.language' )" v-model="profile.private_profile.current_area">
                                      <option>1</option>
                                      <option>2</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-sm-8">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.email' ) }}:</span>
                                    </div>
                                    <input type="text" readonly class="form-control form-control-plaintext" :value="profile.private_profile.email">
                                </div>
                            </div>
                            <div class="col-sm-4">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.email_reminder' ) }}:</span>
                                    </div>
                                    <input type="checkbox" v-model="profile.private_profile.email_reminder" v-on:change="updateUserProfile()">
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.phone_number' ) }}:</span>
                                    </div>
                                    <input type="text" class="form-control form-control-plaintext" v-model="profile.private_profile.phone_number" v-on:change="updateUserProfile()">
                                </div>
                            </div>
                            <div class="col-sm-12">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.main_address' ) }}:</span>
                                    </div>
                                    <input type="text" class="form-control form-control-plaintext" v-model="profile.private_profile.main_address">
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-sm-6">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.current_subscription' ) }}:</span>
                                    </div>
                                    <input type="text" readonly class="form-control form-control-plaintext" :value="profile.internal_profile.current_subscription_type">
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="input-group mt-1">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text">{{ $t( 'profile.subscription_ends_in' ) }}:</span>
                                    </div>
                                    <input type="text" readonly class="form-control form-control-plaintext" :value="profile.internal_profile.subscription_ends_in">
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mt-3">
                                <button type="button" class="btn btn-success btn-lg btn-block">{{ $t('profile.extend_subscription') }}</button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        /* DEBUG */

        <div class="row">
            <div class="col-sm-12">
                {{ profile }} <br>
                {{ languages }}
            </div>
        </div>

        /* TODO: get the related query from ...app_lang */
        
        <div class="row">
            <div class="col-sm-12">
                <p>Bootstrap Vue Form</p>
                <b-form @submit="onSubmit">
                    <b-form-group id="ProfileLanguageInputGroup"
                        label="Language"
                        label-for="ProfileLanguageInput">
                        <b-form-select id="ProfileLanguageInput"

                            :options="languages"
                            required
                            value-field='url' text-field='name'
                            v-model="profile.private_profile.app_lang">
                        </b-form-select>
                    </b-form-group>
                    <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
            </div>
        </div>


    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data: function() {
            return {
                uid: '',
                profile: {
                    'username': '',
                    'public_profile': '',
                    'private_profile': '',
                    'internal_profile': '',
                },
                languages: [],
            }
        },
        methods: {
            onSubmit (evt) {
                evt.preventDefault();
                this.updateUserProfile()
            },
            /* API Endpoints for User Profile */
            getUserProfile: function(){
                var api = `api/myprofile/${this.uid}/`;
                axios.get(api).then((response) => {
                    this.profile = response.data;
                });
            },
            updateUserProfile: function(){
                var api = `api/myprofile/${this.uid}/`;
                axios.put(api, this.profile).then((response) => {
                    this.profile = response.data;
                });
            },
            /* API Endpoints for Language List*/
            listLanguages: function(){
                var api = `api/languages/`;
                axios.get(api).then((response) => {
                    this.languages = response.data;
                });
            },
        },
        computed: {},
        mounted: function() {
            // Get the user id and fetch the User Profile
            this.uid = document.documentElement.getAttribute('uid') || '';
            this.getUserProfile();
            this.listLanguages();
            //console.log(this.profile.private_profile.app_lang);
        }
    }
</script>

<style lang="scss" scoped>
    /* scoped styles*/
    img {
        width:150px;
    }
</style>
