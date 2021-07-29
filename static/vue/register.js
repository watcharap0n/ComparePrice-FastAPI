new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: () => ({
        taxId: '',
        spinProfile: false,
        spinTax: true,
        valid: true,
        taxRules: [
            v => !!v || 'กรุณากรอกหมายเลขภาษี',
            v => Number(v) || 'กรุณากรอกเป็นตัวเลขผู้เสียภาษี',
            v => (v && v.length <= 13 && v.length >= 13 || 'กรุณากรอกหมายเลขผู้เสียภาษีให้ถูกต่้อง')
        ],
        profileLIFF: {
            displayName: '',
            userId: '',
            pictureURL: '',
        },

    }),
    created() {
        liff.init({liffId: '1655717442-np8okjjZ'}, () => {
            if (liff.isLoggedIn()) {
                liff.getProfile()
                    .then(profile => {
                        this.profileLIFF.userId = profile.userId
                        this.profileLIFF.displayName = profile.displayName
                        this.profileLIFF.pictureURL = profile.pictureUrl
                        this.spinProfile = true
                    })
            } else {
                liff.login();
            }
        }, err => console.error(err.code, error.message));
    },
    methods: {
        validate() {
            let form = this.$refs.form.validate();
            let create = {
                userId: this.profileLIFF.userId,
                channel_access_token: '43hrsfYdQjW19sWZT5vOoOSswROHaYTWPENOWqT1WGT0kDkYm3sLsjy+ukGI8cAddcGJsdjUY6RmDCs6Hq+RmuqXqczeAIjU+ABHPHNP4JKLCz5IaFZEN0Qh5oTB2aHzzZWFRqssEsycuMeRI8opqAdB04t89/1O/w1cDnyilFU=',
                site: 'demo',
                topic: 'create_line_token',
                taxcode: this.taxId,
                acct_no: ''
            }
            let find = {
                userId: this.profileLIFF.userId,
                channel_access_token: '43hrsfYdQjW19sWZT5vOoOSswROHaYTWPENOWqT1WGT0kDkYm3sLsjy+ukGI8cAddcGJsdjUY6RmDCs6Hq+RmuqXqczeAIjU+ABHPHNP4JKLCz5IaFZEN0Qh5oTB2aHzzZWFRqssEsycuMeRI8opqAdB04t89/1O/w1cDnyilFU=',
                site: 'demo',
                topic: 'find_customer',
                taxcode: this.taxId
            }
            if (form === true) {
                const path = 'https://service.mangoanywhere.com/anywhere/api/ComparePriceCenter';
                axios.post(path, find)
                    .then((res) => {
                        let data = res.data.data;
                        if (res.data.success === true) {
                            if (data.line_authentication === null) {
                                create.acct_no = data.acct_no
                                axios.post(path, create)
                                    .then((res) => {
                                        Swal.fire(
                                            'บันทึกเรียบร้อย',
                                            'ระบบได้ทำการบันทึกข้อมูล LINE ของท่านเรียบร้อย',
                                            'success'
                                        )
                                            .then(() => {
                                                liff.closeWindow();
                                            })
                                    })
                            } else {
                                Swal.fire({
                                    icon: 'error',
                                    title: 'เกิดข้อผิดพลาด',
                                    text: 'หมายเลขภาษีนี้ได้ทำการลงทะเบียนไปแล้ว',
                                })
                            }
                        } else if (res.data.success === false) {
                            Swal.fire({
                                icon: 'error',
                                title: 'เกิดข้อผิดพลาด',
                                text: res.data.error,
                            })
                        }
                    })
                    .catch((err) => {
                        console.error(err);
                    })
            }
        }
    },
    delimiters: ["[[", "]]"],
})
