new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: (vm) => ({
        clearUrl: true,
        tab: null,
        items: [
            'ข้อมูลเอกสาร', 'แบบไฟล์เอกสาร'
        ],
        spinProfile: false,
        imgFile: null,
        url: null,
        date: new Date().toISOString().substr(0, 10),
        dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
        menu1: false,
        callback: {},
        result: {},
        valid: true,
        userId: '',
        payload: false,
        profileLIFF: {
            displayName: '',
            userId: '',
            pictureURL: '',
        },
        formElements: {
            discount: '',
            cr: '',
            quotation: '',
            payment: '',
            delivery: '',
            specialDiscount: '',
            advance: '',
            guarantee: '',
            remark: '',
            contact: '',
        },
        nameRules: [
            v => !!v || 'is required',
        ],
        email: '',
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        select: null,
        checkbox: false,
    }),
    watch: {
        date(val) {
            this.dateFormatted = this.formatDate(this.date)
        },
    },
    computed: {
        computedDateFormatted() {
            return this.formatDate(this.date)
        },
    },
    beforeCreate() {
        liff.init({liffId: '1655717442-moGlrBB4'}, () => {
            if (liff.isLoggedIn()) {
                liff.getProfile()
                    .then(profile => {
                        liff.getProfile()
                            .then(profile => {
                                this.profileLIFF.userId = profile.userId
                                this.profileLIFF.displayName = profile.displayName
                                this.profileLIFF.pictureURL = profile.pictureUrl
                                this.spinProfile = true
                            })
                        this.getProfile();
                    })
            } else {
                liff.login();
            }
        }, err => console.error(err.code, error.message));
    },
    methods: {
        getProfile() {
            const path = `/getProfile?userId=${this.userId}`;
            axios.get(path)
                .then((res) => {
                    console.log(res.data)
                    this.callback = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        validate() {
            let form = this.$refs.form.validate()
            if (form === true) {
                liff.getProfile()
                    .then(profile => {
                        let to_dict = {
                            userId: profile.userId,
                            discount: this.formElements.discount,
                            cr: this.formElements.cr,
                            quotation: this.formElements.quotation,
                            payment: this.formElements.payment,
                            delivery: this.formElements.delivery,
                            specialDiscount: this.formElements.specialDiscount,
                            advance: this.formElements.advance,
                            guarantee: this.formElements.quotation,
                            remark: this.formElements.remark,
                            contact: this.formElements.contact,
                            date: this.date,
                        }
                        console.log(to_dict)
                        const path = '/index';
                        axios.post(path, to_dict)
                            .then((res) => {
                                console.log(res.data)
                                this.payload = true;
                                this.result = res.data;
                            })
                            .catch((err) => {
                                console.error(err);
                            })
                    })
            }
        },
        formatDate(date) {
            if (!date) return null
            const [year, month, day] = date.split('-')
            return `${day}/${month}/${year}`
        },
        parseDate(date) {
            if (!date) return null
            const [day, month, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
            // return `${day.padStart(2, '0')}-${month.padStart(2, '0')}-${year}`
        },
        previewImage() {
            if (this.imgFile.length >= 1) {
                this.imgFile.forEach((img) => {
                    this.url = URL.createObjectURL(img);
                })
            } else {
                this.url = '';
            }
        },

    },
    delimiters: ["[[", "]]"],
})
