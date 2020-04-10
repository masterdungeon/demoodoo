/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : https://store.webkul.com/license.html/ */

odoo.define('product_price_slots.product_price_slot', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    function load_product_offers(product_id) {
        ajax.jsonRpc("/product/price/slot", 'call', { 'product_id': product_id }
        ).then(function (vals) {
            var $view = $(vals);
            $('.wk_product_offer_slot').html($view);
            $('.wk_product_slot_loading').addClass("hidden");
        });
    }

    $(document).ready(function () {
        var wk_product_id = parseInt($(".wk_product_id").text(), 10);
        if (!wk_product_id) {
            $('.wk_product_slot_loading').removeClass("hidden");
            var product_id = parseInt($(document).find('.js_add_cart_variants').closest('.js_product').find('.product_id').first().val(), 10);
            load_product_offers(product_id);
        }
        $('.oe_website_sale').on('change', 'input.js_variant_change', function (ev) {
            var product_id = parseInt($(ev.target).closest('.js_add_cart_variants').closest('.js_product').find('.product_id').first().val(), 10);
            load_product_offers(product_id);
        });
    });

    
/*     $(document).on('click', '.wk_add_to_cart_slot', function (ev) {
        ev.preventDefault();
        var qty = $(this).closest("form").find(".wk_price_slot_qty").val();
        $('input[name="add_qty"]').val(qty).change().focus().select();
    });
 */

});

odoo.define('product_price_slots.show_price_subtotal', function(require) {
    'use strict';
    
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var utils = require('web.utils');
    var _t = core._t;

    function load_product_subtotal() {
        var wk_product_id = parseInt($(".wk_product_id").text(),10);
        var add_qty = parseInt($('input[name="add_qty"]').val(),10);
        if (add_qty <= 1) {
            $('#show_subtotal').addClass('hidden');
            return false;
        }
        ajax.jsonRpc("/product/price/subtotal", 'call', { 'product_id': wk_product_id, 'add_qty': add_qty }
        ).then(function (vals) {
            var default_price_subtotal = vals.default_price_subtotal;
            var price_subtotal = vals.price_subtotal;
            var html = 'Subtotal: <span style="font-weight:600">$' + price_to_str(price_subtotal) + '</span>';
            if (Math.floor(default_price_subtotal) > Math.floor(price_subtotal)) {
                var saving = default_price_subtotal - price_subtotal;
                if (saving > 0.1) {
                    html += '<span style="display: block; font-size: 14px">You save: ' + '<span class="text-danger" style="font-weight: 600;">$' + price_to_str(saving) + '</span></span>';
                }
            }
            $('#show_subtotal').html(html);
            $('#show_subtotal').removeClass('hidden');
        });
    }

    function price_to_str(price) {
        var l10n = _t.database.parameters;
        var precision = 2;

        if ($(".decimal_precision").length) {
            precision = parseInt($(".decimal_precision").last().data('precision'));
        }
        var formatted = _.str.sprintf('%.' + precision + 'f', price).split('.');
        formatted[0] = utils.insert_thousand_seps(formatted[0]);
        return formatted.join(l10n.decimal_point);
    }

    if(!$('.oe_website_sale').length) {
        return $.Deferred().reject("DOM doesn't contain '.oe_website_sale'");
    }

    $('.oe_website_sale').each(function() {
        var oe_website_sale = this;
        $(oe_website_sale).on('change', 'ul[data-attribute_value_ids]', function(event) {
            load_product_subtotal();
        });
    });

});
