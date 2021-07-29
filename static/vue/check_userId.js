new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: () => ({}),
    beforeCreate() {
        liff.init({liffId: '1655717442-EBWpZqq6'}, () => {
            if (liff.isLoggedIn()) {
                liff.getProfile()
                    .then(profile => {
                        liff.sendMessages([
                            {
                                type: 'text',
                                text: profile.userId
                            }
                        ])
                            .then(() => {
                                console.log(profile.userId)
                                liff.closeWindow();
                            })
                            .catch((err) => {
                                console.log('error', err);
                            });
                    })
            } else {
                liff.login();
            }
        }, err => console.error(err.code, error.message));
    },
    methods: {},
    delimiters: ["[[", "]]"],
})