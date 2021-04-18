package com.project.brandi.data.order

data class Order (
    val userId: String,
    val productId: String,
    val orderDate: String?,
    val status: String?,
)
