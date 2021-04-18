package com.project.brandi.api

import com.project.brandi.data.order.OrderResponse
import com.project.brandi.data.product.ProductResponse
import com.project.brandi.data.user.CreateResponse
import com.project.brandi.data.user.LoginResponse
import okhttp3.RequestBody
import retrofit2.Response
import retrofit2.http.*

// @Query = 파라미터 user?name=dd
// @Path = 경로 user/1  {token}
// @Part = MultiPart form data

interface API {
    @GET("/product/")
    suspend fun getProduct(
    ): Response<ProductResponse>

    @POST("/user/signup/")
    suspend fun signUp(
        @Body user: RequestBody
    ): Response<CreateResponse>

    @POST("/user/signin/")
    suspend fun signIn(
        @Body user: RequestBody
    ): Response<LoginResponse>

    @POST("/order/")
    suspend fun orderProduct(
        @Body order: RequestBody
    ): Response<OrderResponse>
}